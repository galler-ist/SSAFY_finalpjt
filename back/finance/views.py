from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import *
from .models import *
# Create your views here.


def make_financial_data(request):
    DEPOSIT_API_URL =  'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth=162c9dab920fef5a01fbcde0e0ff5759&topFinGrpNo=020000&pageNo=1'
    SAVING_API_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth=162c9dab920fef5a01fbcde0e0ff5759&topFinGrpNo=020000&pageNo=1'
    
    deposit_res = requests.get(DEPOSIT_API_URL).json()
    deposit_baseList = deposit_res.get('result').get('baseList')
    deposit_optionList = deposit_res.get('result').get('optionList')

    for base in deposit_baseList:
        if Deposit.objects.filter(deposit_code = base.get('fin_prdt_cd')):
            continue
        save_product = {
            'deposit_code': base.get('fin_prdt_cd', '-1'),
            'fin_co_no': base.get('fin_co_no', '-1'),
            'kor_co_nm': base.get('kor_co_nm', '-1'),
            'name': base.get('fin_prdt_nm', '-1'),
            'dcls_month': base.get('dcls_month', '-1'),
            'mtrt_int': base.get('mtrt_int', '-1'),
            'etc_note': base.get('etc_note', '-1'),
            'join_deny': base.get('join_deny', -1),
            'join_member': base.get('join_member', '-1'),
            'join_way': base.get('join_way', '-1'),
            'spcl_cnd': base.get('spcl_cnd', '-1'),
            'max_limit': base.get('max_limit', -1),         
        }
        serializer = DepositSerializer(data=save_product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()    
            
    for option in deposit_optionList:
        prdt_cd = option.get('fin_prdt_cd', '-1')
        product = Deposit.objects.get(deposit_code=prdt_cd)
        save_option = {
            'intr_rate_type_nm': option.get('intr_rate_type_nm', '-1'),
            'rsrv_type_nm': option.get('rsrv_type_nm', '-1'),
            'intr_rate': option.get('intr_rate', -1), 
            'intr_rate2': option.get('intr_rate2', -1),
            'save_trm': option.get('save_trm', -1),
        }

        serializer = DepositOptionSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(deposit=product)
    
    saving_res = requests.get(SAVING_API_URL).json()
    saving_baseList = saving_res.get('result').get('baseList')
    saving_optionList = saving_res.get('result').get('optionList')

    for base in saving_baseList:
        if Saving.objects.filter(saving_code=base.get('fin_prdt_cd')):
            continue
        save_product = {
            'saving_code': base.get('fin_prdt_cd', '-1'),
            'fin_co_no': base.get('fin_co_no', '-1'),
            'kor_co_nm': base.get('kor_co_nm', '-1'),
            'name': base.get('fin_prdt_nm', '-1'),
            'dcls_month': base.get('dcls_month', '-1'),
            'mtrt_int': base.get('mtrt_int', '-1'),
            'etc_note': base.get('etc_note', '-1'),
            'join_deny': base.get('join_deny', -1),
            'join_member': base.get('join_member', '-1'),
            'join_way': base.get('join_way', '-1'),
            'spcl_cnd': base.get('spcl_cnd', '-1'),
            'max_limit': base.get('max_limit', -1),
        }
        serializer = SavingSerializer(data=save_product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in saving_optionList:
        prdt_cd = option.get('fin_prdt_cd', '-1')
        product = Saving.objects.get(saving_code=prdt_cd)
        save_option = {
            'intr_rate_type_nm': option.get('intr_rate_type_nm', '-1'),
            'rsrv_type_nm': option.get('rsrv_type_nm', '-1'),
            'intr_rate': option.get('intr_rate', -1),
            'intr_rate2': option.get('intr_rate2', -1),
            'save_trm': option.get('save_trm', -1),
        }

        serializer = SavingOptionSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(saving=product)
    return HttpResponse("금융 데이터 생성 완료")


@api_view(['GET'])
def deposit(request):
    deposits = Deposit.objects.all()
    result = []
    for deposit in deposits:
        serializer = DepositSerializer(deposit)
        options = DepositOption.objects.filter(deposit=deposit)
        option_serializer = DepositOptionSerializer(options, many=True)
        result.append({
            'base': serializer.data,
            'options': option_serializer.data            
        })
    return Response(result)

@api_view(['GET'])
def savings(request):
    savings = Saving.objects.all()
    result = []
    for saving in savings:
        serializer = SavingSerializer(saving)
        options = SavingOption.objects.filter(saving=saving)
        option_serializer = SavingOptionSerializer(options, many=True)
        result.append({
            'base': serializer.data,
            'options': option_serializer.data
        })
    return Response(result)