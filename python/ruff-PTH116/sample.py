# Sample for Ruff rule PTH116: os-stat
# This file is designed to trigger the PTH116 rule.
# Run: ruff check --select PTH116 <this_file>

import os
from pwd import getpwuid
from grp import getgrgid

stat = os.stat(file_name)
owner_name = getpwuid(stat.st_uid).pw_name
group_name = getgrgid(stat.st_gid).gr_name
