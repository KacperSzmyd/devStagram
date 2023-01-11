from .models import Profile
from django.contrib.auth.models import User

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username.title(),
            name=user.first_name.title(),
            email=user.email
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(profile_updated, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)
