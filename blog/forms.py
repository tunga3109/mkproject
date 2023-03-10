from django.forms import CharField, TextInput, EmailInput, EmailField, ModelForm, Textarea, Form
from .models import Comment, Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'type': 'text',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your name'",
                'placeholder': 'Enter your Name'
            }
        ),
        max_length=64
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
        ),
        max_length=254
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control w-100',
                'id': 'message',
                'name': 'message',
                'placeholder': 'Enter Message',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter Message'",
                'cols': '30',
                'rows': '9'

            }
        ),
        max_length=1024
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


class MyForm(Form):
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email'
            }
        ),
        max_length=254
    )


class CommentForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'name': 'name',
                'type': 'text',
                'placeholder': 'Name'
            }
        ),
        max_length=64
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'name': 'email',
                'type': 'email',
                'placeholder': 'Email'
            }
        ),
        max_length=254
    )
    body = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control w-100',
                'id': 'comment',
                'name': 'comment',
                'placeholder': 'Write Comment',
                'cols': '30',
                'rows': '9'

            }
        ),
        max_length=1024
    )

    class Meta:
        model = Comment
        fields = ('body', 'name', 'email')
