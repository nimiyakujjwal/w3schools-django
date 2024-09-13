from django.db import models

# class Model
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(null=True)
    phone = models.IntegerField(null=True)


