# Sample for Ruff rule DJ012: django-unordered-body-content-in-model
# This file is designed to trigger the DJ012 rule.
# Run: ruff check --select DJ012 <this_file>

from django.db import models


class StrBeforeFieldModel(models.Model):
    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"

    def __str__(self):
        return "foobar"

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=40)
