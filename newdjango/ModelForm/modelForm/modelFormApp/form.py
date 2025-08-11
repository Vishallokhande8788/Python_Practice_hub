from django import forms
from .models import modelForm

class modelFormForm(forms.ModelForm):
    class Meta:
        model = modelForm
        fields = '__all__'
        