from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rect3', 'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = Signup
        fields = ['username', 'emailaddress', 'password']  # Include only the fields from your Signup model
        widgets = {
            'username': forms.TextInput(attrs={'class': 'rect', 'placeholder': 'Username'}),
            'emailaddress': forms.EmailInput(attrs={'class': 'rect1', 'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'class': 'rect2', 'placeholder': 'Password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Set password using Django's set_password method
        if commit:
            user.save()
        return user

    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'rect', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rect', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Add your custom authentication logic here
        # For example, if you have a custom user model named CustomUser:
        # if not CustomUser.objects.authenticate(username, password):
        #     raise forms.ValidationError("Invalid username or password")

        # For simplicity, let's assume we're just checking if username and password are not empty
        if not username:
            raise forms.ValidationError("Username cannot be empty")
        if not password:
            raise forms.ValidationError("Password cannot be empty")