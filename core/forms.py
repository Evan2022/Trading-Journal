from allauth.account.forms import LoginForm, SignupForm
from django import forms


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
        self.fields['login'].label = ''
        self.fields['password'].label = ''


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm Password'})
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
