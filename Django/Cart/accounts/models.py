from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings
from products.models import Modelo, Produto, Imagem

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roupas = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return '%s' % (self.user.username)


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

