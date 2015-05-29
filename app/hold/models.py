from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Stock(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Fund(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	rate = models.DecimalField(max_digits=5, decimal_places=2)
	amount = models.DecimalField(max_digits=19, decimal_places=2)
	def __str__(self):
		return self.name

class Hold(models.Model):
	stock = models.ForeignKey(Stock, null=True, blank=True)
	fund = models.ForeignKey(Fund, null=True, blank=True)
	rate = models.DecimalField(max_digits=5, decimal_places=2)
	
	def scode(self):
		return self.stock.code
	scode.short_description = 'Stock Code'
	def fcode(self):
		return self.fund.code
	fcode.short_description = 'Fund Code'
	
	def __str__(self):
		return self.fund.name
