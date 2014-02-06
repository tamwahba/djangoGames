from django.db import models
from django.contrib.auth.models import User


# Model.
class Tokens(models.Model):
    token = models.CharField(max_length=30)


class Sprite(models.Model):
    spriteID = models.CharField(max_length=20)
    xx = models.IntegerField()
    yy = models.IntegerField()
    canInteract = models.BooleanField()

    def __str__(self):
        return self.spriteID


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sprites = models.ManyToManyField(Sprite)
    coins = models.IntegerField(default=0)
#    loggedToken = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username
