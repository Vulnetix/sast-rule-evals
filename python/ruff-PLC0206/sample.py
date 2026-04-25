# Sample for Ruff rule PLC0206: dict-index-missing-items
# This file is designed to trigger the PLC0206 rule.
# Run: ruff check --select PLC0206 <this_file>

ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}

for instrument in ORCHESTRA:
    print(f"{instrument}: {ORCHESTRA[instrument]}")
