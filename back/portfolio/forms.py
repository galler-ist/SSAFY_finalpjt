from django import forms
from .models import Portfolio, SavingOption

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['birth', 'household_size', 'marital_status', 'has_children', 'income', 'savings']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 자녀 계획 필드를 초기에는 숨김
        self.fields['has_children'].widget = forms.HiddenInput()
        self.fields['has_children'].required = False

    def clean(self):
        cleaned_data = super().clean()
        marital_status = cleaned_data.get("marital_status")
        has_children = cleaned_data.get("has_children")

        # 기혼인 경우 자녀 계획 필드를 보여줌
        if marital_status == 'married':
            self.fields['has_children'].widget = forms.CheckboxInput()
            self.fields['has_children'].required = True

        return cleaned_data
