# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import whisper
import time

model = whisper.load_model("base")

 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 5

while True:
    i = int(input("Enter 1 for voice command :-"))

    if i == 1:
        # Start recorder with the given values
        # of duration and sample frequency
        recording = sd.rec(int(duration * freq),
                        samplerate=freq, channels=2)
        
        # Record audio for the given number of seconds
        sd.wait()
        
        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        # print(recording)
        write("audio.wav", freq, recording)
        time.sleep(3)
        result = model.transcribe("./audio.wav")
    
        # Convert the NumPy array to audio file
        # wv.write("recording1.wav", recording, freq, sampwidth=2)