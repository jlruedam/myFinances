from django import views
from django.urls import path
from logBook import views

urlpatterns = [
    path('',views.index, name="index"),
    path('saveEvent/',views.saveEvent, name="saveEvent")
]
