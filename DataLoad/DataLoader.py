from torch.utils.data import Dataset, DataLoader
from scipy.io import wavfile 
from Audio_Compression.utils.audioutil import Audio
import os


class AudioSampleLoader():
    def __init__(self, chunk_dir, chunk_extension):
        self.chunk_loc= os.listdir(chunk_dir+"/.*{}".format(chunk_extension))
        self.len= len(self.chunk_loc)
        self.audio= Audio()
    
    def __len__(self):
        return self.len
    
    def __getitem__(self, index):
        self.audio.read(self.chunk_loc[index])
        pass
Dataset= AudioSampleLoader("/home/fatjuicyboi/paper/Audio-Compression/audio-sample/chunks", "mp3")
print(Dataset.chunk_loc)