import hashlib
import os

import requests
import json
import base64
import torchaudio
import torch

import soundfile
import numpy as np

ANKI_CONNECT_URL = 'http://localhost:8765'

def get_empty_audio_cards():
    query = "audio:"
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": query
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()['result']

def get_note_by_timestamp(timestamp):
    query = f"date:{timestamp}"
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": query
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()['result']

def get_card_fields(note_ids):
    payload = {
        "action": "notesInfo",
        "version": 6,
        "params": {
            "notes": note_ids
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()['result']

def store_audio_to_anki(wav_data, note):
    audio_filename = get_hash_name(note)
    # 保存音频文件
    soundfile.write(audio_filename, np.ravel(wav_data) , 24000)
    # torchaudio.save(audio_filename, torch.from_numpy( wav_data), 24000)

    with open(audio_filename, "rb") as f:
        audio_content = f.read()

    audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    payload = {
        "action": "storeMediaFile",
        "version": 6,
        "params": {
            "filename": audio_filename,
            "data": audio_base64
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    # 删除临时音频文件
    os.remove(audio_filename)

    return response.json()['result']

def get_hash_name(note):
    text = note['fields']['Context']['value']
    # 将文本转换为字节形式
    text_bytes = text.encode('utf-8')

    # 使用 SHA-256 算法生成哈希值
    hash_object = hashlib.sha256(text_bytes)

    # 将哈希值转换为十六进制字符串
    hash_hex = hash_object.hexdigest()

    return f"{hash_hex}.wav"

def update_card_audio(note_id, audio_filename):
    payload = {
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note_id,
                "fields": {
                    "Audio": f"[sound:{audio_filename}]"
                }
            }
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()['result']
