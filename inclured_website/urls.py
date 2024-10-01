from django.contrib import admin
from django.urls import path, include
from inclured1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("inclured1.urls")),
    path('', views.index, name="index")
]
