# Generated by Django 4.0.3 on 2022-03-28 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_destination_picture_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='picture',
            new_name='picture_upload',
        ),
    ]
