from rest_framework import serializers
from .models import Portfolio, SavingOption

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['birth', 'household_size', 'marital_status', 'has_children', 'income']

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = ['id', 'name']