from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Enquiry(models.Model):
    enquiry_des = models.CharField(max_length=1000,null=False)
    name = models.CharField(max_length=100,null=False)
    created_date = models.DateField(default=datetime.date.today)



