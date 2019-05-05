
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tpl1', views.tpl1),
    path('tpl2', views.tpl2),
    path('tpl3', views.tpl3),
]
