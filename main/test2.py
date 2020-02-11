import numpy as np

filename = 'tracks/trainingtrack.npz'
tracks = np.load(filename, allow_pickle=True)
track1 = tracks['track1'].tolist()
track2 = tracks['track2'].tolist()
checkpoints = tracks['checkpoints'].tolist()

for i in range(len(checkpoints)):
    checkpoints[i].pop()
print(checkpoints)

np.savez('trainingtrack.npz', track1=track1, track2=track2, checkpoints=checkpoints)
