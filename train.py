from DataLoad.DataLoader import AudioSampleLoader

Dataset= AudioSampleLoader("/home/fatjuicyboi/paper/Audio-Compression/audio-sample/chunks", "mp3")
print(Dataset.chunk_loc)