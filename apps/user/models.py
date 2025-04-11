# django
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# third
# own


# Create your models here.

class User(models.Model):
    phone = models.CharField(max_length=10, blank=True, null=True)
    mobile_phone = models.CharField(max_length=13, blank=True, null=True)
    direction = models.CharField(max_length=60, blank=True, null=True)
    page = models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='user/image', blank=True, null=True)
    speciality = models.CharField(max_length=150, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.user_id}'

class Skill(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    content = RichTextField()
    image = models.ImageField(upload_to='skills/image')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.title}'

class File(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    content = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return f'{self.title}'