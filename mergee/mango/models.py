from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class User_Prod(models.Model):
    user_id=models.CharField(max_length=70)
    user_name=models.CharField(max_length=70)
    user_product=models.CharField(max_length=70)
    user_price=models.CharField(max_length=70)
    
    class Meta:
        db_table="mergee"

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=30, blank=True)
    phone_no=models.CharField(max_length=12)
    class Meta:
        db_table="profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()