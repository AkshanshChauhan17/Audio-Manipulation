import librosa
from matplotlib import pyplot as plt

audio = 'audio/1.mp3'
x, sr = librosa.load(audio)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))

plt.figure(figsize=(10, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
plt.savefig('output.jpg')

print(x, sr, X, Xdb)