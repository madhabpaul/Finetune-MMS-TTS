import subprocess
from transformers import pipeline
import scipy

synthesizer = pipeline("text-to-speech", model="madhabpaul/mms-tts-asm") # add device=0 if you want to use a GPU

text = "তাজমহলৰ ওপৰত এটা ৰচনা লিখিলোঁ"

speech = synthesizer(text)

scipy.io.wavfile.write("finetuned_output.wav", rate=speech["sampling_rate"], data=speech["audio"][0])