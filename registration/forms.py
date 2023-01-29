from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.authtoken.admin import User
from django.forms import CharField, TextInput, PasswordInput, EmailInput, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your Username'",
                'placeholder': 'Enter your Username'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your Email'",
                'placeholder': 'Enter your Email'
            }
        )
    )
    password1 = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your Password'",
                'placeholder': 'Enter your Password'
            }
        )
    )
    password2 = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password2',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your Password'",
                'placeholder': 'Repeat Password'
            }
        )
    )

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = User


class LoginForm(AuthenticationForm):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your Username'",
                'placeholder': 'Enter your Username'
            }
        )
    )
    password = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your Password'",
                'placeholder': 'Enter your Password'
            }
        )
    )
