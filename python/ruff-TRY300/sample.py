# Sample for Ruff rule TRY300: try-consider-else
# This file is designed to trigger the TRY300 rule.
# Run: ruff check --select TRY300 <this_file>

def get_data():
    try:
        data = fetch()
        return data  # TRY300: move return to else
    except RequestError:
        return None

