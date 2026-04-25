# Sample for Ruff rule DJ003: django-locals-in-render-function
# This file is designed to trigger the DJ003 rule.
# Run: ruff check --select DJ003 <this_file>

from django.shortcuts import render


def index(request):
    posts = Post.objects.all()
    return render(request, "app/index.html", locals())
