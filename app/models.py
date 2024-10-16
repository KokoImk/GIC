from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import CustomUser

APPLICATION_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('reapply', 'Reapply'),
    ]

class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    passport_number = models.CharField(max_length=20, unique=True)
    application_status = models.CharField(max_length=10, choices=APPLICATION_STATUS, default='pending')
    visa_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} Profile"


class AgentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, unique=True)
    contact_number = models.CharField(max_length=20)


class VisaApplication(models.Model):
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    visa_type = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ])
    processing_officer = models.ForeignKey(AgentProfile, null=True, on_delete=models.SET_NULL)


class Document(models.Model):
    visa_application = models.ForeignKey(VisaApplication, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    upload = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Case(models.Model):
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Open')


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} with email {self.email} need support."

class Blog(models.Model):
    image = models.ImageField(upload_to='blog_image', blank=True)
    round_image = models.ImageField(upload_to='blog_image', blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_published = models.BooleanField(default=False,  blank=True, null=True)

    def __str__(self):
        return self.title

class FullPaymentUpload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE, blank=True, null=True)
    full_payment_image = models.ImageField(upload_to="full-payment/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} have upload proof. submitted on {self.submitted_at}"

class Sponsorship(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE, blank=True, null=True)
    sponsorship_payment_image = models.ImageField(upload_to="full-payment/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} have upload proof. submitted on {self.submitted_at}"



