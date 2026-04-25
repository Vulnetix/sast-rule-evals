d = {"a": 1}
if "a" in d:
    del d["a"]  # RUF051: use d.pop("a", None) instead
