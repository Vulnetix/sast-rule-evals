# Sample for Ruff rule RUF041: unnecessary-nested-literal
# This file is designed to trigger the RUF041 rule.
# Run: ruff check --select RUF041 <this_file>

ReadOnlyMode         = Literal["r", "r+"]
WriteAndTruncateMode = Literal["w", "w+", "wt", "w+t"]
WriteNoTruncateMode  = Literal["r+", "r+t"]
AppendMode           = Literal["a", "a+", "at", "a+t"]

AllModes = Literal[ReadOnlyMode, WriteAndTruncateMode,
                  WriteNoTruncateMode, AppendMode]
