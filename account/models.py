from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    image = models.CharField(max_length=100, choices=[
        ('pidgeotpfp.jpg', 'Pidgeot'),
        ('pikachupfp.jpg', 'Pikachu'),
        ('charizardpfp.jpg', 'Charizard'),
        ('blastoisepfp.jpg', 'Blastoise'),
        ('venusaurpfp.jpg', 'Venusaur'),
        ('eeveepfp.jpg', 'Eevee'),
    ], default='pidgeotpfp.jpg')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()