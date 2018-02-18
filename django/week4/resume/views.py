from django.shortcuts import render
from django.http import HttpResponse

from .models import Resume


def resume(request):
    """
    renders the resume page from resume app
    """
    resume = Resume.objects.first()

    return render(request, "resume/resume.html",
        context={"resume": resume})
