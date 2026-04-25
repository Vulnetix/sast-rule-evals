# Sample for Ruff rule TID252: relative-imports
# This file is designed to trigger the TID252 rule.
# Run: ruff check --select TID252 <this_file>

from . import utils  # TID252: prefer absolute imports
from ..models import User

