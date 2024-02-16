from django import forms
from django.forms import ModelForm
from django.forms import ClearableFileInput
from .models import Interview,OFFERS_DETAILS,Candidate,VACANCIES

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = '__all__'
        widgets = {
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }

class HiringForm(ModelForm):
    class Meta:
        model = OFFERS_DETAILS
        fields = '__all__'

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'}),
            'resume' : ClearableFileInput
        }

class vacancyform(ModelForm):
    class Meta:
        model = VACANCIES
        fields = '__all__'





