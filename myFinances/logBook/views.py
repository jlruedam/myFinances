from multiprocessing import context
from django.shortcuts import render
from logBook.models import *

# Create your views here.

def index(request):
    dataEvents=accountingEvent.objects.all()

    context={
        "dataEvents":dataEvents
    }

    return render(request, "logBook/index.html", context)

def saveEvent(request):
    dataEvents=accountingEvent.objects.all()

    dateEvent=request.POST["dateEvent"]
    nameAccount=request.POST["selectAccount"]
    nameSubaccount=request.POST["selectSubAccount"]
    value=request.POST["valueEvent"]
    description=request.POST["descriptionEvent"]

    newEvent=accountingEvent(
        dateEvent=dateEvent,
        account=nameAccount,
        subaccount=nameSubaccount,
        valueEvent=value,
        descriptionEvent=description
    )
    newEvent.save()

    context={
        "dataEvents":dataEvents
    }

    return render(request, "logBook/index.html", context)


