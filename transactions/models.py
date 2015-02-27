from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
	date_created = models.DateField(auto_now_add=True)
	last_modified_date = models.DateField(auto_now=False)
	user_id = models.ForeignKey(User, unique=True)
	buyer = models.PositiveIntegerField()
	transaction_id = models.PositiveIntegerField()
	status = models.CharField(max_length=255)
	status_detail = models.CharField(max_length=255)
	transaction_type = models.CharField(max_length=255)
	marketplace = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=10, decimal_places=3)

