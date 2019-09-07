from speech_to_text.speech_to_text import recorded_speech_recognition, real_time_recognition
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
if not args.no_sound:
        import sounddevice as sd


# Transform speech to text

filename = "auf_widersehen.wav"
audio_path = os.path.join('data', filename)
# recorded_voice = recorded_speech_recognition(audio_path)
recorded_voice = real_time_recognition()

# Translate the text
text = fairseq_translation(recorded_voice)
print(text)

# Read the translated text using the original voice
voice_cloning(audio_path, text, args.enc_model_fpath, args.syn_model_dir, args.voc_model_fpath, args.low_mem)