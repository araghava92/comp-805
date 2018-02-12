from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    description = models.TextField(null=False, blank=False)


class Education(models.Model):
    institution_name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=100, null=False, blank=False)
    major = models.CharField(max_length=100, blank=False)
    gpa = models.FloatField(blank=False)
