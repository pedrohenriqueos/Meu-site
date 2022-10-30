from django.urls import path
from . import views

urlpatterns = [
    path('',views.algorithms,name='algorithms'),
    path('<str:algorithm>/',views.algorithm)
]