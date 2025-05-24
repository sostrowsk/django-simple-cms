from django import forms
from django.core.validators import MinLengthValidator, EmailValidator
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=100,
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={
            'class': 'form-field-default w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your Name',
            'data-validate': 'name'
        })
    )
    
    email = forms.EmailField(
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'class': 'form-field-default w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'your.email@example.com',
            'data-validate': 'email'
        })
    )
    
    subject = forms.CharField(
        min_length=5,
        max_length=200,
        validators=[MinLengthValidator(5)],
        widget=forms.TextInput(attrs={
            'class': 'form-field-default w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Subject',
            'data-validate': 'subject'
        })
    )
    
    message = forms.CharField(
        min_length=10,
        max_length=1000,
        validators=[MinLengthValidator(10)],
        widget=forms.Textarea(attrs={
            'class': 'form-field-default w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your message...',
            'rows': 5,
            'data-validate': 'message'
        })
    )
    
    # Honeypot field for spam protection
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label="Leave empty"
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
    
    def clean_honeypot(self):
        """Check honeypot field is empty."""
        honeypot = self.cleaned_data.get('honeypot')
        if honeypot:
            raise forms.ValidationError("Invalid form submission.")
        return honeypot