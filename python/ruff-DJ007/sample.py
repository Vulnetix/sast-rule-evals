# Sample for Ruff rule DJ007: django-all-with-model-form
# This file is designed to trigger the DJ007 rule.
# Run: ruff check --select DJ007 <this_file>

from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"  # DJ007: specify fields explicitly

