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
    
    
    
    
# 여기부터는 추천알고리즘 함수
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.views.decorators.csrf import csrf_exempt

def calculate_age(birthdate):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def calculate_score(portfolio):
    age = calculate_age(portfolio['birth'])
    
    if 0 <= age <= 29:
        age_score = 0
    elif 30 <= age <= 39:
        age_score = 1
    elif 40 <= age <= 49:
        age_score = 2
    elif 50 <= age <= 59:
        age_score = 3
    else:
        age_score = 4
    
    score = age_score
    
    if portfolio['household_size'] >= 2:
        score += 1
    
    if portfolio['marital_status'] == '기혼' and portfolio['has_children'] >= 1:
        score += 1
    
    return score

@require_POST
@csrf_exempt
def portfolio_score(request):
    try:
        data = json.loads(request.body)
        birth = data.get('birth')
        household_size = data.get('household_size')
        marital_status = data.get('marital_status')
        has_children = data.get('has_children')
        income = data.get('income')

        # Check for missing required fields
        if not birth or household_size is None or not marital_status or has_children is None or income is None:
            return JsonResponse({'error': 'Missing required parameters'}, status=400)

        portfolio = {
            'birth': birth,
            'household_size': int(household_size),
            'marital_status': marital_status,
            'has_children': int(has_children),
            'income': float(income)
        }

        score = calculate_score(portfolio)
        return JsonResponse({'score': score})

    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
