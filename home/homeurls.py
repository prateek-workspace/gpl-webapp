from django.urls import path
from . import views
#write your urls path here
urlpatterns=[

    path('',views.index,name='index'),

]