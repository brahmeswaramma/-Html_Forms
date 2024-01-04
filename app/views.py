from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']        
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)

        
    return render(request,'insert_topic.html')


def insert_webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpages.objects.get_or_create(topic_name=TO,name=n,url=ur,email=em)[0]
        WO.save()
        WQLO=Webpages.objects.all()
        d1={'webpages':WQLO}
        return render(request,'display_webpages.html',d1)
    return render(request,'insert_webpages.html',d)



def insert_access_records(request):
    QLWO=Webpages.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        n=request.POST['n']
        a=request.POST['a']
        d=request.POST['d']

        WO=Webpages.objects.get(name=n)
        ARO=Access_Records.objects.get_or_create(name=WO,author=a,date=d)[0]
        ARO.save()
        QLARO=Access_Records.objects.all()
        d1={'records':QLARO}
        return render(request,'display_access_record.html',d1)
    return render(request,'insert_access_records.html',d)


def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d1={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpages.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpages.objects.filter(topic_name=i)
        d2={'webpages':QLWO}
        return render(request,'display_webpages.html',d2)
    
    return render(request,'select_multiple_webpage.html',d1)


def select_multiple_accessrecord(request):
    QLWO=Webpages.objects.all()
    d1={'webpages':QLWO}
    if request.method=='POST':
        webpagelist=request.POST.getlist('wn')
        QLAO=Access_Records.objects.none()
        for i in webpagelist:
            QLAO=QLAO|Access_Records.objects.filter(name=i)
        d2={'accessrecords':QLAO}
        return render(request,'display_access_record.html',d2)
    return render(request,'select_multiple_accessrecord.html',d1)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkbox.html',d)

