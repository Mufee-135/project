from django import forms
from .models import Profile, PortfolioItem, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'skills', 'contact_details']

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['title', 'description',  'link']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description',  'link']
