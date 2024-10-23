from django.contrib import admin
from django.urls import path, include
from inclured1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("inclured1.urls")),
    path('', views.index, name="index"),
    # path('login/', views.user_login, name='login'),  # Vista de login
    # path('logout/', views.user_logout, name='logout'),  # Vista de logout
]
