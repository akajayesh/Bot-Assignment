from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_wlc_email(user_email):
    send_mail(
        subject='Welcome to our platform!',
        message='Thank you for Registering!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )
    return f"Sent Welcome Email to {user_email}"