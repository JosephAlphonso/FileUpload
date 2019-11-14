from django.db import models
from django.core.validators import RegexValidator


class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True)
    dob = models.DateField()
    age = models.IntegerField()
    def __str__(self):
        return "%s" %(self.name)