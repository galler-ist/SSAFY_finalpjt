from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomRegisterSerializer
from dj_rest_auth.registration.views import RegisterView

# Create your views here.

@csrf_exempt
def user_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        data = {
            'username': user.username,
            # 'nickname': user.nickname, # 이거 바꿈
            'last_login': user.last_login
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = CustomRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer