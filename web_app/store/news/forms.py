from .models import *
from django.forms import ModelForm, TextInput, NumberInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class AnimalsForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя животного'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Возраст животного'}))
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    color = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Animals
        fields = ['name', 'age', 'cat', 'color']


class ColorsForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Цвет животного'}))


    class Meta:
        model = Color
        fields = ['name']


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите логин'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Повторите пароль'}))
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the role'}), initial='user')

    class Meta:
        model = User
        fields = ["username","first_name", "last_name","email", "password1", "password2", "role"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите логин'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите email'}))
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите роль"}))

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "role"]

