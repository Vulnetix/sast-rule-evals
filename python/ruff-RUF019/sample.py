dct = {"key": "value"}
if "key" in dct and dct["key"]:  # RUF019: use dct.get("key") instead
    pass
