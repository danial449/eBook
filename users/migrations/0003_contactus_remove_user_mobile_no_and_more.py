# Generated by Django 5.1 on 2024-08-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_email_verification_token_user_is_email_verified_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="mobile_no",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="mobile_no",
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
