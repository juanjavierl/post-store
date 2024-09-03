from django import forms

from core.pos.models import *

class ClientFormOrder(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        exclude = ('gender','birthdate','email',)
        #fields = '__all__'