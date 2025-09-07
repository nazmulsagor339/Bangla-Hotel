from django.urls import path,include

from core.views import home, menu, tracking, reservation

urlpatterns = [
    path('',home,name='home'),
    path('menu/',menu,name='menu'),
    path('tracking/',tracking,name='tracking'),
    path('reservation/',reservation,name='reservation'),
]