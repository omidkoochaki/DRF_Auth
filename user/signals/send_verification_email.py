from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import ActivationCode
from user.tasks import send_email

User = get_user_model()


@receiver(signal=post_save, sender=ActivationCode)
def ask_celery_send_email(sender, instance, created, **kwargs):
    if created and not instance.user.is_email_verified:
        send_email.delay(email=instance.user.email, code=instance.code)

