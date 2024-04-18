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

class profileData(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["bio","phone_no"]
        widgets={
            "bio":forms.TextInput(attrs={'class':"form-control"}),
            "phone_no":forms.TextInput(attrs={'class':"form-control"}),
        }
