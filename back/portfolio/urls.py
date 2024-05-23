from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, PortfolioByUsernameView

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
# router.register(r'saving-options', SavingOptionViewSet)

app_name = 'portfolio'
urlpatterns = [
    path('', include(router.urls)),
    path('api/user/<str:username>/', PortfolioByUsernameView.as_view(), name='portfolio-by-username'),
]
