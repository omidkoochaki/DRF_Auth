from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import ActivationCode
from user.tasks import send_otp

User = get_user_model()


@receiver(signal=post_save, sender=ActivationCode)
def ask_celery_send_otp(sender, instance, created, **kwargs):
    if created and not instance.user.is_mobile_verified:
        send_otp.delay(number=instance.user.mobile, code=instance.code)

