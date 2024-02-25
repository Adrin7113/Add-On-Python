from django.db import models


# Create your models here.
class ContactUsModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    message = models.TextField(max_length=500)
    place = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class LoginModel(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username


class RegModel(models.Model):
    FName = models.CharField(max_length=25)
    LName = models.CharField(max_length=25)
    PhoneNo = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.FName
