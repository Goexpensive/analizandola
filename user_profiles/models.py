from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User,primary_key=True)

    # Other fields here
    user_external_reference = models.IntegerField(null=True)
    token = models.CharField(max_length=255,null=True)
    refresh_token = models.CharField(max_length=255,null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save(self, *args, **kwargs):
    if not self.pk:
        try:
            p = UserProfile.objects.get(user=self.user)
            self.pk = p.pk
        except UserProfile.DoesNotExist:
            pass

    super(UserProfile, self).save(*args, **kwargs)        

post_save.connect(create_user_profile, sender=User)