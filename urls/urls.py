from django.urls import path

from . import views

app_name = 'urls'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<slug:short_url>/', views.short_url, name='short_url'),
]
