import os
import wave
from piper import PiperVoice

# 1. Path to your downloaded model files
model_path = "en_US-lessac-medium.onnx"
config_path = "en_US-lessac-medium.onnx.json"

# 2. Load the neural voice engine
voice = PiperVoice.load(model_path, config_path=config_path)

text = "Wow! I am speaking with realistic inflection and natural word stress. This sounds so much better than pyttsx3!"
output_file = "output.wav"

# 3. Open the file in write-binary mode and let Piper build the structure
with wave.open(output_file, "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print(f"Success! Expressive audio saved to {output_file}")
