from django.urls import path, include
from .views import UserProfileView, CustomRegisterView

app_name='accounts'
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # path('signup/', CustomRegisterView.as_view(), name='custom_signup'),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
]