# Sample for Ruff rule ICN002: banned-import-alias
# This file is designed to trigger the ICN002 rule.
# Run: ruff check --select ICN002 <this_file>

import tensorflow.keras.backend as K
