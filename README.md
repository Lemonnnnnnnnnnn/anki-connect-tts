# install 
```
git clone https://github.com/Lemonnnnnnnnnnn/anki-connect-tts
cd anki-connect-tts
pip install -r requirements.txt
pip install coqui-tts 
```

# Use

## premise
run anki with [ankiConnect](https://ankiweb.net/shared/info/2055492159)

## generate all audio for the notes with the field "audio" is empty 
python main.py --add

## generate audio for specific note, specific note with the field "Date" value
python main.py --update 1692684879893

## attention

Card template derive from [saladict](https://github.com/crimx/ext-saladict), the default text to generate the audio is field "Context", the default save field is "Audio".

# Thanks

- thanks for [saladict](https://github.com/crimx/ext-saladict)
- thanks for [chattts](https://github.com/2noise/ChatTTS)
- thanks for ChatGpt