# Sample for Ruff rule DJ001: django-nullable-model-string-field
# This file is designed to trigger the DJ001 rule.
# Run: ruff check --select DJ001 <this_file>

from django.db import models

class Profile(models.Model):
    bio = models.TextField(null=True)  # DJ001: use blank=True

