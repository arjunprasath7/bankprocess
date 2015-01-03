from django.db import models
from datetime import datetime  

# Create your models here.

class User(models.Model):
	username	=	models.CharField(max_length=200)
	address		=	models.TextField();
	password 	=	models.CharField(max_length=200)

class Transaction(models.Model):
	userId			=	models.ForeignKey(User)
	withdrawal		=	models.IntegerField()
	deposit			=	models.IntegerField()
	balance			=	models.IntegerField()
	TransactionDate	=	models.DateTimeField(default=datetime.now(),blank=True)

