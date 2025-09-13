from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .validators import validate_strong_password

User = get_user_model()

class PersonalInfoForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address'
        })
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1234567890'
        })
    )
    address = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter your address'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("This username is already taken.")
        return username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            phone = phone.replace(' ', '').replace('-', '')
            if User.objects.filter(phone=phone).exists():
                raise forms.ValidationError("This phone number is already registered.")
        return phone

class PasswordForm(forms.Form):
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password (min 12 chars)'
        }),
        validators=[validate_strong_password]
    )
    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            validate_strong_password(password1)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match.")
        
        return cleaned_data

class ProfileForm(forms.Form):
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        }),
        help_text="Optional. Maximum file size: 5MB. Supported formats: JPG, PNG, GIF"
    )

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            if profile_picture.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File size cannot exceed 5MB.")
            
            allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg']
            if profile_picture.content_type not in allowed_types:
                raise forms.ValidationError("Only JPG, PNG, and GIF files are allowed.")
        
        return profile_picture

class ConsentForm(forms.Form):
    terms_accepted = forms.BooleanField(
        required=True,
        label="I accept the terms and conditions",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        error_messages={
            'required': 'You must accept the terms and conditions to proceed.'
        }
    )

    def clean_terms_accepted(self):
        terms_accepted = self.cleaned_data.get('terms_accepted')
        if not terms_accepted:
            raise forms.ValidationError("You must accept the terms and conditions to proceed.")
        return terms_accepted