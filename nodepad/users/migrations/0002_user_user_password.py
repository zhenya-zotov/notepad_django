# Generated by Django 5.0.1 on 2024-01-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_password",
            field=models.CharField(default="test_password", max_length=25),
        ),
    ]
