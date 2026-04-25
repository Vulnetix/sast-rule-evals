# Sample for Ruff rule PLW0711: binary-op-exception
# This file is designed to trigger the PLW0711 rule.
# Run: ruff check --select PLW0711 <this_file>

try:
    pass
except TypeError or ValueError:  # PLW0711: use tuple
    pass

