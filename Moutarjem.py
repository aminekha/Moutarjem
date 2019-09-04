from speech_to_text.speech_to_text import recorded_speech_recognition
from translate.translator import fairseq_translation
from demo_cli import voice_cloning
import os
import argparse
from utils.argutils import print_args
from pathlib import Path

## Info & args
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-e", "--enc_model_fpath", type=Path, 
                    default="encoder/saved_models/pretrained.pt",
                    help="Path to a saved encoder")
parser.add_argument("-s", "--syn_model_dir", type=Path, 
                    default="synthesizer/saved_models/logs-pretrained/",
                    help="Directory containing the synthesizer model")
parser.add_argument("-v", "--voc_model_fpath", type=Path, 
                    default="vocoder/saved_models/pretrained/pretrained.pt",
                    help="Path to a saved vocoder")
parser.add_argument("--low_mem", action="store_true", help=\
    "If True, the memory used by the synthesizer will be freed after each use. Adds large "
    "overhead but allows to save some GPU memory for lower-end GPUs.")
parser.add_argument("--no_sound", action="store_true", help=\
    "If True, audio won't be played.")
args = parser.parse_args()
print_args(args, parser)



# Transform speech to text

filename = "LDC93S1.wav"
audio_path = os.path.join('data', filename)
recorded_voice = recorded_speech_recognition(audio_path)

# Translate the text
text = fairseq_translation(recorded_voice)
print(text)

# Read the translated text using the original voice
voice_cloning(args)