from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:short_url>/', views.short_url, name='short_url')
]
