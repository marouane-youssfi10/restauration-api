# Generated by Django 3.2.11 on 2022-06-23 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "male"), ("female", "female")],
                        max_length=20,
                        null=True,
                        verbose_name="gender",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=30, region=None, verbose_name="phone number"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="address"
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        max_length=50, verbose_name="country"
                    ),
                ),
                ("city", models.CharField(max_length=50, verbose_name="city")),
                (
                    "profile_photo",
                    models.ImageField(upload_to="", verbose_name="profile photo"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
    ]
