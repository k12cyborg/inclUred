from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informacion/', views.informacion, name='informacion'),
    path('cursos/', views.cursos, name='cursos'),
    path('videos/', views.videos_informativos, name='videos_informativos'),
    path('anecdotas/', views.anecdotas, name='anecdotas'),
]
