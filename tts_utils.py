import ChatTTS

# 初始化 ChatTTS
chat = ChatTTS.Chat()
chat.load(compile=False)  # compile=True for better performance

def infer_audio(texts):
    wavs = []
    for i in range(0, len(texts), 5):  # Process texts in batches of 5
        batch = texts[i:i+5]
        batch_wavs = chat.infer(batch)
        wavs.extend(batch_wavs)
    return wavs
