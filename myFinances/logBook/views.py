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
