# Sample for Ruff rule S610: django-extra
# This file is designed to trigger the S610 rule.
# Run: ruff check --select S610 <this_file>

from django.contrib.auth.models import User

# String interpolation creates a security loophole that could be used
# for SQL injection:
User.objects.all().extra(select={"test": "%secure" % "nos"})
