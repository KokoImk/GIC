from django.urls import path
from app.views import *

app_name = "app"

urlpatterns = [
    path('', index , name="index"),
    path('more_countries/', view_more_country , name="more_countries"),
    path('contact/', contact , name="contact"),
    path('dashboard/', dashboard , name="dashboard"),
    path('profile/', profile , name="profile"),
    path('upload_documents/', upload_documents , name="upload_documents"),
    path('payment_proof/', payment_proof , name="payment_proof"),
    path('sponsorship_payment_proof/', sponsorship_payment_proof , name="sponsorship_payment_proof"),
    path('about_us/', about_us , name="about_us"),
    path('assessment_form/', assessment_form , name="assessment_form"),
    path('details/<int:country>', detail_page , name="detail_page"),
]

