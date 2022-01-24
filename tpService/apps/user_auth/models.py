from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """用户类拓展"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="avatar")
    role = models.CharField(max_length=10, default="editor", verbose_name="role")
    introduction = models.TextField(max_length=500, null=True, blank=True, verbose_name="introduction")

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.user.__str__())
