from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=None, null=False, blank=False)
    location = models.CharField(max_length=None, null=False, blank=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
