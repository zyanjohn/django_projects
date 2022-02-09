from django import forms
from app1.models import student
class studentform(forms.ModelForm):  #Form Definition
    class Meta:
        model=student
        fields='__all__'