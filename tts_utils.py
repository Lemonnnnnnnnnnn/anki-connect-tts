import torch
from TTS.api import TTS
import random

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"  # 选择你需要的模型

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
tts = TTS(model_name=MODEL_NAME).to(device)

# 获取可用的音色列表（根据模型的不同可能会有所不同）
available_voices = tts.speakers

# 随机选择一个音色
selected_voice = random.choice(available_voices)

print("selected_voice",selected_voice)

def infer_audio(texts: list):
    # Run TTS
    # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # Text to speech list of amplitude values as output
    wavs = []
    for text in texts:
        wav = tts.tts(text=text, speaker=selected_voice,language="en")
        wavs.append(wav)

    return wavs

