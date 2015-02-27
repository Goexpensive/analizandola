from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    date_created = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=False)
    metric_type = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, unique=True)

