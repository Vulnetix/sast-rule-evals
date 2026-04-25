# Sample for Ruff rule DJ006: django-exclude-with-model-form
# This file is designed to trigger the DJ006 rule.
# Run: ruff check --select DJ006 <this_file>

from django import forms

class MyForm(forms.ModelForm):
    class Meta:
        exclude = "__all__"  # DJ006

