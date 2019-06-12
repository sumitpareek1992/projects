from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	user_type=[('e',"Employee"),('m',"Manager")]
	phone=models.CharField(max_length=10)
	type=models.CharField(choices=user_type, max_length=1)
class LeaveType(models.Model):
	name=models.CharField(max_length=200)
	count=models.IntegerField()
class Leave(models.Model):
	desc=models.TextField(blank=True, null=True)
	type=models.ForeignKey(LeaveType, on_delete=models.PROTECT)
	date=models.DateTimeField(default=datetime.now)
	user=models.ForeignKey(User, on_delete=models.PROTECT)
