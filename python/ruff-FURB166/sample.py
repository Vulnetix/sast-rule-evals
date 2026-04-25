# Sample for Ruff rule FURB166: int-on-sliced-str
# This file is designed to trigger the FURB166 rule.
# Run: ruff check --select FURB166 <this_file>

num = "0xABC"

if num.startswith("0b"):
    i = int(num[2:], 2)
elif num.startswith("0o"):
    i = int(num[2:], 8)
elif num.startswith("0x"):
    i = int(num[2:], 16)

print(i)
