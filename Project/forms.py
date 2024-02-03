from django import forms
from.models import Data

class Input(forms.ModelForm):
    class Meta:
        model=Data
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(Input, self).__init__(*args, **kwargs)
        self.fields['Password'].widget = forms.PasswordInput()