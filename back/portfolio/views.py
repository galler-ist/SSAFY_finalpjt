from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import Portfolio, SavingOption
from .serializers import PortfolioSerializer, SavingOptionSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
# Create your views here.

# class PortfolioViewSet(viewsets.ModelViewSet):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer
#     permisson_classes = [IsAuthenticated]    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

# class PortfolioCreateView(generics.CreateAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class PortfolioByUsernameView(generics.RetrieveUpdateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        try:
            portfolio = Portfolio.objects.get(user=user)
        except Portfolio.DoesNotExist:
            raise NotFound("Portfolio not found")

        return portfolio



class SavingOptionViewSet(viewsets.ModelViewSet):
    queryset = SavingOption.objects.all()
    serializer_class = SavingOptionSerializer
    
    
class PortFolioSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer    