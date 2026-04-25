# Sample for Ruff rule D204: incorrect-blank-line-after-class
# This file is designed to trigger the D204 rule.
# Run: ruff check --select D204 <this_file>

class PhotoMetadata:
    """Metadata about a photo."""
    def __init__(self, file: Path):
        ...
