import pickle

def load_data(file_path):
    with open(file_path, "rb") as f:
        # VNX-PY-003: pickle.load with untrusted data
        data = pickle.load(f)
    return data

def from_bytes(raw):
    # VNX-PY-003: pickle.loads
    return pickle.loads(raw)
