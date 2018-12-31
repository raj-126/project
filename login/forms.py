from django import forms
from .models import (
    Profiles,
    ProfilesBank
)

class ProfilesForm(forms.ModelForm):

    class Meta:
        model = Profiles
        exclude = ('id',)

class searchForm(forms.Form):

    search = forms.CharField(
        max_length= 20,
        label   = "Please Do search Here"
    )

    # def clean_search(self, *args, **kwargs):
    #     raise forms.ValidationError("Tu Gando Che")12