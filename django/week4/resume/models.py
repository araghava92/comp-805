from django.db import models

# Resume model
class Resume(models.Model):
    # Table fields
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    def get_full_name(self):
        """
        returns full name of the person in the form "Firstname Lastname"
        """
        return "{} {}".format(self.first_name, self.last_name)

    def get_last_name_first_name(self):
        """
        returns name in the form "Lastname, Firstname"
        """
        return "{}, {}".format(self.last_name, self.first_name)

    def get_education(self):
        """
        returns education for the person defined in the education table
        """
        return self.education_set.all()

    def get_experience(self):
        """
        returns experience for the person defined in the experience table
        """
        return self.experience_set.all()

# Experience model
class Experience(models.Model):
    # ForeignKey relationship field
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)

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
    # ForeignKey relationship field
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)

    institution_name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=100, null=False, blank=False)
    major = models.CharField(max_length=100, blank=False)
    gpa = models.FloatField(blank=False)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.institution_name, self.location,
            self.degree, self.major, self.gpa)
