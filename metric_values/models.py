from django.db import models
from django.contrib.auth.models import User
from metrics.models import Metric

class MetricValue(models.Model):
    date_created = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=False)
    user_id = models.ForeignKey(User, unique=True)
    metric_type_id = models.ForeignKey(Metric, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=3)
