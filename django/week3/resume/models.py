from django.db import models

# Experience model
class Experience(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.title, self.location,
            self.start_date, self.end_date, self.description)

# Education model
class Education(models.Model):
    institution_name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=100, null=False, blank=False)
    major = models.CharField(max_length=100, blank=False)
    gpa = models.FloatField(blank=False)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.institution_name, self.location,
            self.degree, self.major, self.gpa)
