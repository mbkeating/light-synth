import pyaudio
from Synth.ISynth import ISynth
import numpy as np
import math

class SimpleSynth(ISynth):
    def __init__(self):
        self.audio = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,  
            channels=1,              
            rate=44100, 
            output=True, 
            frames_per_buffer=256
        )
        
    def play(self, notes): 
        """
        Sine wave oscillator
        """
        duration = 0.2
        sample_rate = 44100
        num_samples = int(sample_rate * duration)
        
        waveform = np.zeros(num_samples)
        for note in notes:
            osc = 0.5 * np.sin(2 * np.pi * note * np.arange(num_samples) / sample_rate)
            waveform += osc
        
        waveform = np.clip(waveform / len(notes), -1, 1)
        self.audio.write(np.int16(32767 * waveform).tobytes())