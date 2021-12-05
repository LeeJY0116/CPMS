from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Profile(models.Model):
    objects = models.Manager
    userName = models.CharField(max_length=10)
    userID = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=30)
    bool_logIO = models.BooleanField(default=False)

    def __str__(self):
        return self.userName

class MyTicket(models.Model):
    # Profile 데이터베이스랑 종속
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null = False,
    )
    objects = models.Manager
    myTicket = models.TextField()
    myPaymentDetails = models.TextField()

    def __str__(self):
        return str(self.profile) + "\'s ticket"
