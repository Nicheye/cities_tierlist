from django.db import models

# Create your models here.
class City(models.Model):
	A='A'
	B='B'
	C='C'
	D='D'
	E='E'
	TIER_CHOICES =[
		(A,'A'),
		(B,'B'),
		(C,'C'),
		(D,'D'),
		(E,'E'),
	]
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=500)
	tier = models.CharField(max_length=1,choices=TIER_CHOICES,default=A)
	date = models.DateTimeField(auto_now=True)