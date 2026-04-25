# Sample for Ruff rule DJ008: django-model-without-dunder-str
# This file is designed to trigger the DJ008 rule.
# Run: ruff check --select DJ008 <this_file>

from django.db import models


class MyModel(models.Model):
    field = models.CharField(max_length=255)
