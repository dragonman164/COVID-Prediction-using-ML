from django import forms
from django.http.request import QueryDict
from .models import CovidSymptomps


class CovidSymptopmsForm(forms.ModelForm):
    class Meta:
        model = CovidSymptomps
        fields = '__all__'
        widgets ={
            'cough':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'fever':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'sore_throat':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'shortness_of_breadth':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'head_ache':forms.CheckboxInput(attrs={'class':'form-check-input'}),            
        }