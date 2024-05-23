from rest_framework import serializers
from .models import CustomUser
from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer

class CustomRegisterSerializer(DefaultRegisterSerializer):
    nickname = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'nickname')

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data.get('nickname')
        user.email = self.validated_data.get('email')
        user.save()
        return user