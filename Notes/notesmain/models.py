from django.db import models

# Create your models here.
class notedata(models.Model):
	ntopic=models.CharField(max_length=100)
	ndetail=models.CharField(max_length=1000)
	ndate=models.CharField(max_length=20)
	