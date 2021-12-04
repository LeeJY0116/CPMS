from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Profile(models.Model):
    objects = models.Manager
    userName = models.CharField(max_length=10)
    userID = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=30)

class MyTicket(models.Model):
    # Profile 데이터베이스랑 종속
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null = False,
    )
    objects = models.Manager
    myTicket = ArrayField(ArrayField(models.TextField()))
    myPaymentDetails = ArrayField(ArrayField(models.TextField()))
