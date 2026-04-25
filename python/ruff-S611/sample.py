# Sample for Ruff rule S611: django-raw-sql
# This file is designed to trigger the S611 rule.
# Run: ruff check --select S611 <this_file>

from django.db.models.expressions import RawSQL
from django.contrib.auth.models import User

User.objects.annotate(val=RawSQL("%s" % input_param, []))
