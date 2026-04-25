# vnx-py-018 eval target
import tempfile
import os

# TRIGGERS: tempfile.mktemp() has a TOCTOU race condition
def write_temp_file(data):
    tmp_path = tempfile.mktemp(suffix=".json")
    with open(tmp_path, "w") as f:
        f.write(data)
    return tmp_path

# Safe alternative:
# with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
#     f.write(data)
#     return f.name
