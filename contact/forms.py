from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-secondary border border-gray-700 focus:border-accent focus:outline-none',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-secondary border border-gray-700 focus:border-accent focus:outline-none',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-secondary border border-gray-700 focus:border-accent focus:outline-none',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-secondary border border-gray-700 focus:border-accent focus:outline-none',
                'placeholder': 'Your Message',
                'rows': 6
            }),
        }
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message should be at least 10 characters long.")
        return message
