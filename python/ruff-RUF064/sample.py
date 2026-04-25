import os

os.chmod("file.txt", 644)  # RUF064: should be 0o644 (octal)
