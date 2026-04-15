import yaml

def load_config(path):
    with open(path) as f:
        # VNX-PY-004: yaml.load without SafeLoader
        config = yaml.load(f)
    return config
