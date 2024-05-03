from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('homecreat/',views.homecreat,name='homecreat'),
    path('rentercreat/',views.rentercreat,name='rentercreat'),
    path('homelist/',views.homelist,name='homelist')


    
]