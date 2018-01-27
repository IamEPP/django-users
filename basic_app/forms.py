from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    """ Form """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        """Meta"""
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    """Te"""
    class Meta:
        """Meta class for UserProfileInfo"""
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
