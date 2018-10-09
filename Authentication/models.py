from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Task(models.Model):
    Task_name = models.CharField(max_length=255, blank=True, null=True)
    Employee_name = models.CharField(max_length=255, blank=True, null=True)
    Employee_Id = models.IntegerField(unique=True)
    mobile_number = models.IntegerField(unique=True)
    # models.DateTimeField(_('created date'), auto_now_add=True)
    created_date = models.DateTimeField()

    def __str__(self):
        return str(self.Task_name)