from django import forms
from django.contrib.auth.models import User   # Importing system defined model from django Admin named "User"
from basic_app.models import UserProfileInfo    # Importing Developer defined model from django named "UserProfileInfo"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
