import ChatTTS

# 初始化 ChatTTS
chat = ChatTTS.Chat()
chat.load(compile=True)  # compile=True for better performance

def infer_audio(texts):
    wavs = chat.infer(text= texts, lang='en')
    return wavs
