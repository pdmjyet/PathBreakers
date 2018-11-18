from django.shortcuts import render
from .Models.PathBreaker import PathBreaker, Profession

def home(request):
    return render(request, "PathBreakers/HomePage.html")

def pathbreakers(request):
    pathbreakersList = []
    professionsList = []
    yog = request.GET.get('yog', None)
    profession = request.GET.get('profession', None)
    dataOnly = request.GET.get('dataOnly', None)
    if yog is not None and profession is not None :
        pathbreakersList = PathBreaker.objects.filter(yog=yog, Profession__name = profession)
    elif yog is not None:
        pathbreakersList = PathBreaker.objects.filter(yog=yog)
    elif profession is not None:
        pathbreakersList = PathBreaker.objects.filter(Profession__name = profession)
    else:
        pathbreakersList = PathBreaker.objects.all()

    professionsList = Profession.objects.all()
    yogsList = PathBreaker.objects.order_by().values('yog').distinct()
    context = {
        "path_breakers_list": pathbreakersList,
        "profession_list": professionsList,
        "yog_list": yogsList
    }
    if dataOnly is not None:
        return pathbreakersList;
    return render(request, "PathBreakers/PathBreakersPage.html", context)