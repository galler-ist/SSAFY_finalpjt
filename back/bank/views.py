from django.shortcuts import render
from django.http import JsonResponse
# from .models import Bank
import requests

# Create your views here.

# 기본 지도 보여주기
def index(request):
    return render(request,'bank/index.html')

# 필터링된 지도 보여주기
def filtered_banks(request):
    city = request.GET.get('city')
    district = request.GET.get('district')
    bank_name = request.GET.get('name')

    query = f"{city} {district} {bank_name}"

    headers = {
        'Authorization': 'KakaoAK 053d9b9ffc2deb571c11f5fb73bdbeb2'
    }
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"

    response = requests.get(url, headers=headers)
    data = response.json()

    banks = []

    if 'documents' in data:
        for place in data['documents']:
            banks.append({
                'name': place['place_name'],
                'latitude': place['y'],
                'longitude': place['x'],
                'address': place['address_name'],
                'road_address': place.get('road_address_name'),
                'phone': place.get('phone'),
                'category_name': place.get('category_name'),
                'place_url': place.get('place_url')                
            })
    return JsonResponse(banks, safe=False)

#TODO: 마커 찍기
#TODO: 은행들 데이터 api로 따오기

#TODO: bank model 만들고 그걸 JsonResponse로 받아와야함
#TODO: 데이터를 추가????????????? 나는 데이터를 추가하는게 아니라 pinia에다가 넣고 할거야
#TODO: API 엔드포인트 생성..?