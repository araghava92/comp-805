from django.shortcuts import render


def home(request):
    """
    returns home page
    """
    return render(request, "home.html", None)
