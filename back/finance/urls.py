"""
URL configuration for my_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name= 'finance'

router= DefaultRouter()
router.register(r'deposits', views.DepositViewSet)
router.register(r'savings', views.SavingViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('deposit/', views.deposit, name='deposit'),
    path('savings/', views.savings, name='savings'),
    path('make_financial_data/', views.make_financial_data),
]

