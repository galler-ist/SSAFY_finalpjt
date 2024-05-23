from rest_framework import serializers
from .models import Portfolio, SavingOption
from finance.models import Deposit, Saving
from accounts.models import CustomUser

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = ['id', 'name']
        
        
        
class FinanceDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class FinanceSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

class DepositListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['deposit_code', 'kor_co_nm', 'name']

class SavingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = ['saving_code', 'kor_co_nm', 'name']


class PortfolioSerializer(serializers.ModelSerializer):
    deposits = DepositListSerializer(many=True)
    savings = SavingListSerializer(many=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Portfolio
        fields = ['user', 'username', 'birth', 'household_size', 'marital_status', 'has_children', 'income', 'deposits', 'savings']
        read_only_fields = ['user', 'username']

    def create(self, validated_data):
        deposits_data = validated_data.pop('deposits')
        savings_data = validated_data.pop('savings')
        user = self.context['request'].user
        portfolio = Portfolio.objects.create(user=user, **validated_data)
        for deposit_data in deposits_data:
            deposit = Deposit.objects.get(deposit_code=deposit_data['deposit_code'])
            portfolio.deposits.add(deposit)
        for saving_data in savings_data:
            saving = Saving.objects.get(saving_code=saving_data['saving_code'])
            portfolio.savings.add(saving)
        return portfolio

    def update(self, instance, validated_data):
        deposits_data = validated_data.pop('deposits')
        savings_data = validated_data.pop('savings')

    def update(self, instance, validated_data):
        deposits_data = validated_data.pop('deposits')
        savings_data = validated_data.pop('savings')

        instance.deposits.clear()
        for deposit_data in deposits_data:
            deposit = Deposit.objects.get(deposit_code=deposit_data['deposit_code'])
            instance.deposits.add(deposit)

        instance.savings.clear()
        for saving_data in savings_data:
            saving = Saving.objects.get(saving_code=saving_data['saving_code'])
            instance.savings.add(saving)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    
    
