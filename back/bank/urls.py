from django.urls import path
from . import views

app_name = 'bank'
urlpatterns = [
    path('',views.index, name='index'),
    path('filtered/',views.filtered_banks, name='filtered_banks'),
]
