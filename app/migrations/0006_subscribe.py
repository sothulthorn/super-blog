# Generated by Django 5.1.4 on 2025-01-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_comments_parent"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscribe",
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
                ("email", models.EmailField(max_length=100)),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
    ]
