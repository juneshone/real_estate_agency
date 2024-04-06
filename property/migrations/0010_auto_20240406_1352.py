# Generated by Django 2.2.24 on 2024-04-06 10:52

import phonenumbers

from django.db import migrations


def change_phonenumbers_format(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber_parts = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(phonenumber_parts):
            owner_pure_phone = phonenumbers.format_number(phonenumber_parts, phonenumbers.PhoneNumberFormat.E164)
            flat.owner_pure_phone = owner_pure_phone
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_auto_20240406_1237'),
    ]

    operations = [
        migrations.RunPython(change_phonenumbers_format),
    ]