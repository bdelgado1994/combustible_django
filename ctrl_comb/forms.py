from django import forms
from ctrl_comb.models import *

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields="__all__"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class":"form-control"
            })