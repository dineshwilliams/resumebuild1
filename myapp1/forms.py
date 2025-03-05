from django import forms
from .models import Resume, Education, Experience, Skill,create

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'address', 'objective']

class createForm(forms.ModelForm):
    class Meta:
        model = create
        fields= '__all__'

