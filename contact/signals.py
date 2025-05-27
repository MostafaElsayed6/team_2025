from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactMessage
from django.core.mail import send_mail

@receiver(post_save, sender=ContactMessage)
def send_notification(sender, instance, **kwargs):
    send_mail(
        'رسالة جديدة من الموقع',
        f'تم استلام رسالة جديدة من {instance.name} ({instance.email})',
        'noreply@example.com',
        ['admin@example.com'],
        fail_silently=False,
    )