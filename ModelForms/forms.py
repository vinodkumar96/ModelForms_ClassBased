from django import forms
from .models import product

class productform (forms.ModelForm):
    class Meta:
        model=product
        fields=['p_id','p_name','p_cost','p_mfd','p_exd']
