from speech_to_text.speech_to_text import recorded_speech_recognition
from translate.translator import fairseq_translation

recorded_voice = recorded_speech_recognition("data/LDC93S1.wav")

text = fairseq_translation(recorded_voice)
print(text)