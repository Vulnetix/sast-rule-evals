# Sample for Ruff rule DJ013: django-non-leading-receiver-decorator
# This file is designed to trigger the DJ013 rule.
# Run: ruff check --select DJ013 <this_file>

from django.dispatch import receiver
from django.db.models.signals import post_save


@transaction.atomic
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    pass
