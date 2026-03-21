from django import forms
from .models import Scenario, TestCase


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ['title', 'description', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['title', 'steps', 'expected_result', 'actual_result', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'steps': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 2
            }),
            'expected_result': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 2
            }),
            'actual_result': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 2
            }),
            'status': forms.Select(attrs={
                'class': 'form-select form-select-sm'
            }),
        }