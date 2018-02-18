from datetime import date
from django.test import TestCase

from .models import Education, Experience, Resume

class ResumeTest(TestCase):
    resume = Resume(first_name="Raghava", last_name="Adusumilli")
    education = Education(institution_name = "UNH", location = "MHT",
        degree = "MS", major = "IT", gpa = 3.8)
    experience = Experience(title = "SDE", location = "MHT",
        start_date = date.today(), end_date = date.today(),
        description = "SDE at MHT")

    def setUp(self):
        self.resume.save()
        self.education.save()
        self.experience.save()

    def test_get_full_name(self):
        """
        Tests get_full_name method of Resume model class
        """
        self.assertEqual(self.resume.get_full_name(), "Raghava Adusumilli")

    def test_get_last_name_first_name(self):
        """
        Tests get_last_name_first_name method of Resume model class
        """
        self.assertEqual(self.resume.get_last_name_first_name(),
            "Adusumilli, Raghava")

    def test_get_experience(self):
        """
        Tests get_experience method of Resume model class
        """
        self.assertEqual(self.resume.get_experience().first(),
            self.experience)

    def test_get_education(self):
        """
        Tests get_education method of Resume model class
        """
        self.assertEqual(self.resume.get_education().first(), self.education)
