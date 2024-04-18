from django import forms
from mango.models import User_Prod, Profile

class Data(forms.ModelForm):
    class Meta:
        model=User_Prod
        fields="__all__"
        widgets={
            "user_id":forms.TextInput(attrs={'class':"form-control"}),
            "user_product":forms.TextInput(attrs={'class':"form-control"}),
            "user_price":forms.TextInput(attrs={'class':"form-control"}),
            "user_name":forms.TextInput(attrs={'class':"form-control"})
        }

class ProfileData(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)
    class Meta:
        model=Profile
        fields=["bio","phone_no"]
        widgets={
            "bio":forms.TextInput(attrs={'class':"form-control"}),
            "phone_no":forms.TextInput(attrs={'class':"form-control"}),
        }

def __init__(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super(ProfileData, self).__init__(*args, **kwargs)
        if user_instance:
            self.user_instance = user_instance
            self.fields['username'] .initial = user_instance.username
            self.fields['password'].widget.attrs['placeholder'] = 'Enter new password'