from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   
    path('',views.news_home,name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/',views.NewsDetailView.as_view(),name='news_detail'),

    ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)