from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Youth, Adult

class YouthSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['email', 'title', 'first_name', 'last_name', 'phone', 'address', 'mosque', 'password1', 'password2']

    def save_youth(self):
        user = super().save(commit=False)
        user.is_youth = True
        user.save()
        Youth.objects.create(user=user)
        return user

class AdultSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['email', 'title', 'first_name', 'last_name', 'phone', 'address', 'mosque', 'password1', 'password2']

    def save_adult(self):
        user = super().save(commit=False)
        user.is_adult = True
        user.save()
        Adult.objects.create(user=user)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)