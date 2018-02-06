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


def portfolio(request):
    """
    returns portfolio Homepage
    """
    portfolio = [
        dict(
            name= "Project 1", company= "Company 1", duration= "8 weeks",
            description= "Worked using various opensource technologies",
        ),
        dict(
            name= "Project 2", company= "Company 2", duration= "8 weeks",
            description= "Worked using various opensource technologies",
        ),
        dict(
            name= "Project 3", company= "Company 3", duration= "8 weeks",
            description= "Worked using various opensource technologies",
        ),
    ]
    return render(request, "portfolio.html", context={"portfolio": portfolio})


def contact(request):
    """
    returns contact us page
    """
    return render(request, "contact.html", context={"url": request.path})
