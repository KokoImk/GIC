# Generated by Django 4.2.8 on 2024-09-09 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgentProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("agency_name", models.CharField(max_length=255)),
                ("license_number", models.CharField(max_length=50, unique=True)),
                ("contact_number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="ApplicantProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nationality", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("passport_number", models.CharField(max_length=20, unique=True)),
                (
                    "application_status",
                    models.CharField(default="Pending", max_length=50),
                ),
                ("visa_type", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="blog_image")),
                ("round_image", models.ImageField(blank=True, upload_to="blog_image")),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField()),
                ("published_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "is_published",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.IntegerField(blank=True, null=True)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="VisaApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("visa_type", models.CharField(max_length=100)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.applicantprofile",
                    ),
                ),
                (
                    "processing_officer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.agentprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("document_type", models.CharField(max_length=100)),
                ("upload", models.FileField(upload_to="documents/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "visa_application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.visaapplication",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Case",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(default="Open", max_length=50)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.agentprofile",
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.applicantprofile",
                    ),
                ),
            ],
        ),
    ]
