from django import forms
from app.models import *


class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = ['nationality', 'date_of_birth', 'passport_number', 'application_status', 'visa_type']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'subject', 'message']

class UploadPaymentForm(forms.ModelForm):
    class Meta:
        model = FullPaymentUpload
        fields = ['full_payment_image', ]

        widgets = {
            'full_payment_image': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control image-upload',
                    'accept': 'image/*',
                }
            ),
        }

class SponsorshipPaymentForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        fields = ['sponsorship_payment_image', ]
        widgets = {
            'sponsorship_payment_image': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control image-upload',
                    'accept': 'image/*',
                }
            ),
        }

