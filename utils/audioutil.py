from pydub import AudioSegment
from pydub.utils import make_chunks
import pydub
import numpy as np
from random import randint

class Audio():
    def __init__(self):
        pass

    def make_chunks(self, audio_loc, chunk_save_loc, chunk_length_ms, iden):
        if(iden== None):
            iden= str(randint(1, 1000))
        print("Audio loaded")
        myaudio = AudioSegment.from_file(audio_loc , "mp3") 
        chunks = make_chunks(myaudio, chunk_length_ms)
        for i, chunk in enumerate(chunks):
            chunk_name = chunk_save_loc+ iden+"chunk{0}.mp3".format(i)
            print("exporting", chunk_name)
            chunk.export(chunk_name, format="mp3")

    def read(self, f, normalized=False):
        a = pydub.AudioSegment.from_mp3(f)
        y = np.array(a.get_array_of_samples())
        if a.channels == 2:
            y = y.reshape((-1, 2))
        if normalized:
            return a.frame_rate, np.float32(y) / 2**15
        else:
            return a.frame_rate, y

    def write(self, f, sr, x, normalized=False):
        channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
        if normalized:
            y = np.int16(x * 2 ** 15)
        else:
            y = np.int16(x)
        song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
        song.export(f, format="mp3", bitrate="320k")