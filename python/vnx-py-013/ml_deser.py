# VNX-PY-013: ML/AI insecure deserialization
import torch
import pickle
import numpy as np

model = torch.load("model.pt")
data = pickle.load(open("data.pkl", "rb"))
arr = np.load("data.npy", allow_pickle=True)
