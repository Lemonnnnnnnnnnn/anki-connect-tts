import torch
from TTS.api import TTS

MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"  # 选择你需要的模型

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
tts = TTS(model_name=MODEL_NAME).to(device)

def infer_audio(texts: list):
    # Run TTS
    # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # Text to speech list of amplitude values as output
    wavs = []
    for text in texts:
        wav = tts.tts(text=text)
        wavs.append(wav)

    return wavs

