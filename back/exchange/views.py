from django.shortcuts import render
from rest_framework.response import Response
from .models import Exchange
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .serializers import ExchangeSerializer

# Create your views here.


EXCHANGE_API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=bQejh15dx4FXuA52WqlekvGRQMuVomFU&searchdata=20240520&data=AP01'

@api_view(['GET'])
def index(request):
    try:
        response = requests.get(EXCHANGE_API_URL)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return Response({"error": "Error fetching data from API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if not isinstance(data, list):
        return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)

    exist_response = Exchange.objects.all()
    
    # exist_response가 있으면 지워주고 / serializer 해줌
    if data:
        if exist_response:
            Exchange.objects.all().delete()
            
        serializer = ExchangeSerializer(data=data, many=True)
        
        if not serializer.is_valid():
            print('검증오류 serializer.errors : ',serializer.errors)  # 검증 오류를 로그로 출력
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data)

    return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)