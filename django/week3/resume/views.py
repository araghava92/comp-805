from django.shortcuts import render
from django.http import HttpResponse

from .models import Education as edu
from .models import Experience as exp


def resume(request):
    """
    renders the resume page from resume app
    """
    exp_set = exp.objects.all().order_by("-end_date")
    edu_set = edu.objects.all()

    return render(request, "resume/resume.html",
        context={"exp_set": exp_set, "edu_set": edu_set})
