import ChatTTS
from nemo_text_processing.text_normalization.normalize import Normalizer

# 创建一个Normalizer实例
normalizer = Normalizer(lang='en', input_case='cased')

# 初始化 ChatTTS
chat = ChatTTS.Chat()
chat.load(compile=True)  # compile=True for better performance
try:
    chat.normalizer.register("en", normalizer.normalize)
except ValueError as e:
    print(e)

def infer_audio(texts):
    wavs = chat.infer(text= texts, lang='en')
    return wavs
