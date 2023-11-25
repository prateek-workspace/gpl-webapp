from django.urls import path
from . import views
#write your urls path here
urlpatterns=[

    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('contactus/',views.contactus,name='contactus'),
    path('registration/',views.registration,name='registration'),

]