from speech_to_text.speech_to_text import recorded_speech_recognition
from translate.translator import fairseq_translation
from demo_cli import voice_cloning
import os
# Transform speech to text

filename = "LDC93S1.wav"
audio_path = os.path.join('data', filename)
recorded_voice = recorded_speech_recognition(audio_path)

# Translate the text
text = fairseq_translation(recorded_voice)
print(text)

# Read the translated text using the original voice
voice_cloning(audio_path, text)