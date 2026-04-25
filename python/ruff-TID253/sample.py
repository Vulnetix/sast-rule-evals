# Sample for Ruff rule TID253: banned-module-level-imports
# This file is designed to trigger the TID253 rule.
# Run: ruff check --select TID253 <this_file>

import tensorflow as tf


def show_version():
    print(tf.__version__)
