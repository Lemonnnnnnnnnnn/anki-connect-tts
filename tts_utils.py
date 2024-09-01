from melo.api import TTS


def infer_audio(texts: list, model: TTS):
    wavs = []
    speaker_ids = model.hps.data.spk2id
    speed = 1.0

    for text in texts:
        wav = model.tts_to_file(text, speaker_ids['EN-US'], speed=speed)
        wavs.append(wav)

    return wavs
