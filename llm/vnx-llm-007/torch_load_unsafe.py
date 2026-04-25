# vnx-llm-007 eval target
import torch

# TRIGGERS: torch.load() without weights_only=True allows arbitrary code execution
def load_model_bad(model_path):
    model = torch.load(model_path)
    return model

# TRIGGERS: torch.load() with map_location but still no weights_only
def load_model_with_device(model_path, device):
    model = torch.load(model_path, map_location=device)
    return model

# Safe alternative: use weights_only=True (PyTorch >= 1.13)
# model = torch.load(model_path, weights_only=True)
#
# Or use safetensors format:
# from safetensors.torch import load_file
# weights = load_file(model_path)
