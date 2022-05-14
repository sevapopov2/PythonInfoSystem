from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

ACCOUNT_TYPES = [
    ('student', 'Ученик'),
    ('teacher', 'Преподаватель'),
]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Имя', required=True)
    last_name = forms.CharField(max_length=30, label='Фамилия', required=True)
    email = forms.EmailField(max_length=200, required=True)
    account_type = forms.CharField(label='Выберите тип учётной записи', widget=forms.RadioSelect(choices=ACCOUNT_TYPES))

class meta:
    model = User
    fields = ["first_name", "last_name", "email", "password1", "password2", "account_type"]