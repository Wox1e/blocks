from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import Users

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Users


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ("username", "first_name", "last_name", "email")
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class":"form - control",
                "placeholder":"Username"
            }
        )
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class":"form - control",
                "placeholder":"First name"
            }
        )
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class":"form - control",
                "placeholder":"Last Name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs = {
                "class":"form - control",
                "placeholder":"Email"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class":"form - control",
                "placeholder":"Password"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class":"form - control",
                "placeholder":"Confirm Password"
            }
        )
    )

    
    

    