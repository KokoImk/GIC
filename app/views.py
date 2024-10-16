from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import *
from app.forms import *

from django.contrib.auth import get_user_model
CustomUser = get_user_model()


@login_required
def index(request):
    blogs = Blog.objects.all()[:3]

    context = {
        'blogs': blogs
    }
    return render(request, 'app/index.html', context)

def view_more_country(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'app/view_countries.html', context)

def detail_page(request, country):
    detail = get_object_or_404(Blog, pk=country)

    context = {
        'detail': detail
    }
    return render(request, 'app/detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            check_form = form.save(commit=False)
            # check_form.user = request.user
            check_form.save()
            messages.info(request, 'Upload was successful, your request is being attended to.')
            return redirect('app:contact')
        else:
            form = ContactForm()

    return render(request, 'app/contact.html')

def dashboard(request):
    user = request.user

    data = {
        'user': user,
    }

    return render(request, 'app/dashboard.html', data)


def profile(request):

    return render(request, 'app/profile.html')

def upload_documents(request):
    return render(request, 'app/upload-documents.html')

def about_us(request):
    return render(request, 'app/about_us.html')

def assessment_form(request):
    applicant = ApplicantProfile.objects.filter(user=request.user)
    form = ApplicantProfileForm()
    if applicant.exists():
        messages.warning(request, 'You can only have one document. If you want to change it, do well to contact the admin.')
        return redirect('app:contact')
    else:
        if request.method == 'POST':
            form = ApplicantProfileForm(request.POST)

            if form.is_valid():
                check_form = form.save(commit=False)
                check_form.user = request.user
                check_form.save()
                messages.success(request, 'Upload was successful, your details are being verified. it will take 3 working days!')
                return redirect('app:assessment_form')
            else:
                form = ApplicantProfileForm()

    return render(request, 'app/assessment-documents.html', {'form': form})


def payment_proof(request):
    form = UploadPaymentForm()

    if request.method == 'POST':
        form = UploadPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = request.user

            # Get the ApplicantProfile for the current user
            applicant_profile = request.user.applicantprofile
            check_form.applicant = applicant_profile

            # Save the form (either new or updated)
            check_form.save()
            messages.success(request, 'Upload was successful, your details are being verified.')
            return redirect('app:payment_proof')

    return render(request, 'app/payment_proof.html', {'form': form})


def sponsorship_payment_proof(request):
    form = SponsorshipPaymentForm()

    if request.method == 'POST':
        form = SponsorshipPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = request.user

            # Get the ApplicantProfile for the current user
            applicant_profile = request.user.applicantprofile
            check_form.applicant = applicant_profile

            # Save the form (either new or updated)
            check_form.save()
            messages.success(request, 'Upload was successful, your details are being verified.')
            return redirect('app:sponsorship_payment_proof')

    return render(request, 'app/sponsorship_payment_proof.html', {'form': form})

