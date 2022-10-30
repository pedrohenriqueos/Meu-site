from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('algorithms/',include('algorithms.urls')),
    path('databases/',include('databases.urls')),
    path('server/',include('servers.urls')),
]
