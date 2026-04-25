d = {}
if d.get("key", []):  # RUF056: falsy fallback in dict.get used in boolean context
    print("found")
