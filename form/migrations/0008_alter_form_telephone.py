# Generated by Django 4.0.2 on 2022-02-26 11:27

import django.core.validators
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_rename_user_id_form_user_alter_form_google_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
