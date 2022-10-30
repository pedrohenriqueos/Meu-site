from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.databases,name='databases'),
    path('formulario/',views.formulario),
    path('formulario/create/',views.create),
    path('usuarios',views.usuarios),
    path('<int:user>/',views.user)
]