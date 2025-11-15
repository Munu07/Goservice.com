from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Customer, ServiceProvider, ProviderService,  Booking
from main.models import Service

# ------------------------------
# Customer Signup Form
# ------------------------------
class CustomerSignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_pic', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'customer'
        if commit:
            user.save()
            Customer.objects.create(user=user)
        return user


# ------------------------------
# Service Provider Signup Form
# ------------------------------
class ProviderSignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_pic', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'provider'
        if commit:
            user.save()
            ServiceProvider.objects.create(user=user)
        return user


# ------------------------------
# Admin Login Form
# ------------------------------
class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



class ProviderServiceForm(forms.ModelForm):
    service_type = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        empty_label="Select Service",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = ProviderService
        fields = ['service_type', 'address', 'phone', 'experience', 'price']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter service address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price per hour', 'min': 0, 'step': 0.01}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['schedule_date', 'timing']
        widgets = {
            'schedule_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'timing': forms.Select(attrs={'class': 'form-select'}),
        }