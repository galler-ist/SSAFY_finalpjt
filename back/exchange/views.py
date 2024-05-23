from django.shortcuts import render
from rest_framework.response import Response
from .models import Exchange
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .serializers import ExchangeSerializer

# Create your views here.


EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=bQejh15dx4FXuA52WqlekvGRQMuVomFU&searchdata=20240522&data=AP01'


@api_view(['GET'])
def index(request):
    exist_response = Exchange.objects.all()
    
    if exist_response.exists():
        serializer = ExchangeSerializer(exist_response, many=True)
        return Response(serializer.data)
    
    try:
        response = requests.get(EXCHANGE_API_URL)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return Response({"error": "Error fetching data from API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not isinstance(data, list):
        return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)

    if data:
        Exchange.objects.all().delete()
        
        serializer = ExchangeSerializer(data=data, many=True)
        
        if not serializer.is_valid():
            print('Validation error serializer.errors:', serializer.errors)  # Log validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data)

    return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)