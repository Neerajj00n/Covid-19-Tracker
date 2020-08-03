from django.db import models
from datetime import datetime
# Create your models here.
class Covid19(models.Model):
	country = models.CharField(max_length=100)
	confirmed = models.IntegerField(default=0,blank=True,null=True)
	active = models.IntegerField(default=0,blank=True,null=True)
	recovered = models.IntegerField(default=0,blank=True,null=True)
	deaths = models.IntegerField(default=0,blank=True,null=True)
	new_cases = models.IntegerField(default=0,blank=True,null=True)
	new_deaths = models.IntegerField(default=0,blank=True,null=True )
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.country)

