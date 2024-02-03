from django.urls import path
from .import views

urlpatterns =[
  path('',views.index),
  path('about/',views.about,name="about"),
  path('motor/',views.motor,name="motor"),
  path('motorsmall/',views.motorsmall)
]