# Generated by Django 5.0.1 on 2024-01-22 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note",
            old_name="caption",
            new_name="note_caption",
        ),
        migrations.RenameField(
            model_name="note",
            old_name="create_data",
            new_name="note_create_data",
        ),
        migrations.RenameField(
            model_name="note",
            old_name="text",
            new_name="note_text",
        ),
        migrations.RenameField(
            model_name="note",
            old_name="user",
            new_name="note_user",
        ),
    ]
