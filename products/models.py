from django.db import models
from django import forms
# Create your models here.
class Product(models.Model):
	long_text = models.CharField("",max_length=200,blank=False)
	short_text = models.CharField("",max_length=200,blank=False)
