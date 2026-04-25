# Sample for Ruff rule S202: tarfile-unsafe-members
# This file is designed to trigger the S202 rule.
# Run: ruff check --select S202 <this_file>

import tarfile
import tempfile

tar = tarfile.open(filename)
tar.extractall(path=tempfile.mkdtemp())
tar.close()
