# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-PY-016: Django mass assignment via request data unpacking

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # VULNERABLE: fields='__all__' exposes every model field for writing
        # Attacker can set is_staff=True, is_superuser=True via POST body
        fields = "__all__"

def create_user(request):
    # VULNERABLE: mass assignment via **request.data
    # Attacker can POST {"username": "hacker", "is_staff": true, "is_superuser": true}
    user = User.objects.create(**request.data)
    return user

def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    # VULNERABLE: mass assignment via **request.POST
    User.objects.filter(id=user_id).update(**request.data)
    return user
