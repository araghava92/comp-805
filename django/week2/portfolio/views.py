from django.shortcuts import render


def home(request):
    """
    returns home page
    """
    return render(request, "home.html", context=None)


def resume(request):
    """
    returns resume page
    """
    # Resume Content
    resume = dict(
        name= "raghava",
        email= "email@example.com",
        phone= "(xxx) xxx-xxxx",
        summary= "Worked as a Full stack developer for 4 years"
    )
    return render(request, "resume.html", context={"resume": resume})
