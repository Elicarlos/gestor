from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.CursoList.as_view(), name='cursos-list'),

]