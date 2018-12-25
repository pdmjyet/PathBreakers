from django.shortcuts import render
from .Models.PathBreaker import PathBreaker, Profession
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.db.models import F

def home(request):
    return render(request, "PathBreakers/HomePage.html")

def pathbreakers(request):
    pathbreakersList = []
    professionsList = []
    yog = request.GET.get('yog', None)
    profession = request.GET.get('profession', None)
    dataOnly = request.GET.get('dataOnly', None)
    if yog is not None and profession is not None :
        yog = int(yog)
        pathbreakersList = PathBreaker.objects.filter(yog__range=(yog, yog+10), Profession__name = profession)
    elif yog is not None:
        yog = int(yog)
        pathbreakersList = PathBreaker.objects.filter(yog__range=(yog, yog+10))
    elif profession is not None:
        pathbreakersList = PathBreaker.objects.filter(Profession__name = profession)
    else:
        pathbreakersList = PathBreaker.objects.all()

    if yog is not None:
        yog = int(yog)
        professionsList = PathBreaker.objects.filter(yog__range=(yog, yog+10)).order_by().values('Profession__name').distinct()
    else:
    #    professionsList = PathBreaker.objects.order_by().values('Profession__name').distinct()
        professionsList = Profession.objects.annotate(Profession__name = F('name')).values('Profession__name')

    yogsList = PathBreaker.objects.order_by().values('yog').distinct()
    context = {
        "path_breakers_list": pathbreakersList,
        "profession_list": professionsList,
        "yog_list": getYogRangeList(yogsList)
    }
    #if dataOnly is not None:
    #    qs_json= serializers.serialize('json', pathbreakersList)
    #    #return HttpResponse(qs_json, content_type='application/json')
    #    return render(request, "PathBreakers/PathBreakersList.html", context)

    return render(request, "PathBreakers/PathBreakersPage.html", context)


def getProfessions(request):
    professionsList = []
    yog = request.GET.get('yog', None)
    if yog is not None:
        yog = int(yog)
        professionsList = PathBreaker.objects.filter(yog__range=(yog, yog+10)).order_by().values('Profession__name').distinct()
    else:
        professionsList = PathBreaker.objects.order_by().values('Profession__name').distinct()
    return JsonResponse({'response' :  list(professionsList)})

def getYogRangeList(yogList):
    minVal = -1;
    maxVal = -1;
    for yogObj in yogList:
        if minVal == -1 and maxVal == -1 :
            minVal = yogObj['yog']
            maxVal = yogObj['yog']

        elif yogObj['yog'] < minVal:
            minVal = yogObj['yog']
        elif yogObj['yog'] > maxVal:
            maxVal = yogObj['yog']

    minRange = (minVal // 10) * 10
    maxRange = (maxVal // 10) * 10 +10
    return  list(range(minRange, maxRange + 10, 10))
