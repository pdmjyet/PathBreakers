from django.shortcuts import render
from .Models.PathBreaker import PathBreaker
from .Models.Profession import  Profession, ProfessionTag
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.db.models import F

def home(request):
    return render(request, "PathBreakers/HomePage.html")

def pathbreakers(request, college):
    pathbreakersList = []
    professionsList = []
    tagsList = []
    print(college)
    yog = request.GET.get('yog', None)
    profession = request.GET.get('profession', None)
    tag = request.GET.get('tag', None)
    dataOnly = request.GET.get('dataOnly', None)

    if yog is not None and profession is not None and tag is not None:
        yog = int(yog)
        pathbreakersList = PathBreaker.objects.filter(yog__range=(yog, yog+10), professionTag__profession__name = profession, professionTag__tag = tag)
    elif yog is not None and profession is not None :
        yog = int(yog)
        pathbreakersList = PathBreaker.objects.filter(yog__range=(yog, yog+10), professionTag__profession__name = profession)
    elif yog is not None and tag is not None:
        yog = int(yog)
        pathbreakersList = PathBreaker.objects.filter(yog__range=(yog, yog+10), professionTag__tag = tag)
    elif profession is not None and tag is not None:
        pathbreakersList = PathBreaker.objects.filter(professionTag__profession__name = profession, professionTag__tag = tag)
    elif yog is not None:
        yog = int(yog)
        pathbreakersList = PathBreaker.objects.filter(yog__range=(yog, yog+10))
    elif profession is not None:
        pathbreakersList = PathBreaker.objects.filter(professionTag__profession__name = profession)
    elif tag is not None:
        pathbreakersList = PathBreaker.objects.filter(professionTag__tag = tag)
    else:
        pathbreakersList = PathBreaker.objects.all()

    if yog is not None:
        yog = int(yog)
        professionsList = Profession.objects.filter(professiontag__pathbreaker__yog__range=(yog, yog+10)).values('name').distinct()
        if profession is not None:
            tagsList = ProfessionTag.objects.filter(pathbreaker__yog__range=(yog, yog + 10),
                                                    profession__name=profession).values('tag').distinct()
        else:
            tagsList = ProfessionTag.objects.filter(pathbreaker__yog__range=(yog, yog + 10)).values('tag').distinct()
    else:
        professionsList = Profession.objects.values('name')
        if profession is not None:
            tagsList = ProfessionTag.objects.filter(profession__name=profession).values('tag').distinct()
        else:
            tagsList = ProfessionTag.objects.all().values('tag').distinct()

    yogsList = PathBreaker.objects.order_by().values('yog').distinct()
    context = {
        "path_breakers_list": pathbreakersList,
        "profession_list": professionsList,
        "yog_list": getYogRangeList(yogsList),
        "tags": tagsList
    }
    #if dataOnly is not None:
    #    qs_json= serializers.serialize('json', pathbreakersList)
    #    #return HttpResponse(qs_json, content_type='application/json')
    #    return render(request, "PathBreakers/PathBreakersList.html", context)

    return render(request, "PathBreakers/PathBreakersPage.html", context)


def getProfessions(request):
    professionsList = []
    yog = request.GET.get('yog', None)
    profession = request.GET.get('profession', None)
    if yog is not None and profession is not None:
        yog = int(yog)
        professionsList = Profession.objects.filter(professiontag__pathbreaker__yog__range=(yog, yog + 10), name = profession).values('name').distinct()
        tagsList = ProfessionTag.objects.filter(pathbreaker__yog__range=(yog, yog + 10), profession__name = profession).values('tag').distinct()
    elif yog is not None:
        yog = int(yog)
        professionsList = Profession.objects.filter(professiontag__pathbreaker__yog__range=(yog, yog + 10)).values('name').distinct()
        tagsList = ProfessionTag.objects.filter(pathbreaker__yog__range=(yog, yog + 10)).values('tag').distinct()
        #professionsList = PathBreaker.objects.filter(yog__range=(yog, yog+10)).order_by().values('Profession__name').distinct()
    elif profession is not None:
        professionsList = Profession.objects.filter(name = profession).values('name').distinct()
        tagsList = ProfessionTag.objects.filter(profession__name = profession).values('tag').distinct()
    else:
        professionsList = Profession.objects.values('name')
        tagsList = ProfessionTag.objects.values('tag').distinct()
        #professionsList = PathBreaker.objects.order_by().values('Profession__name').distinct()
    return JsonResponse({'response' :  { 'professions' : list(professionsList), 'tags' : list(tagsList) }})

def getTags(request):
    professionsList = []
    yog = request.GET.get('yog', None)
    if yog is not None:
        yog = int(yog)
        professionsList = Profession.objects.filter(professiontag__pathbreaker__yog__range=(yog, yog + 10)).values('name').distinct()
        #professionsList = PathBreaker.objects.filter(yog__range=(yog, yog+10)).order_by().values('Profession__name').distinct()
    else:
        professionsList = Profession.objects.values('name')
        #professionsList = PathBreaker.objects.order_by().values('Profession__name').distinct()
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

    if minVal is -1:
        return []
    minRange = (minVal // 10) * 10
    maxRange = (maxVal // 10) * 10 +10
    return  list(range(minRange, maxRange + 10, 10))
