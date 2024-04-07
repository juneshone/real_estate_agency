# Generated by Django 2.2.24 on 2024-04-06 19:56

from django.db import migrations


def connect_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        owner_flats = Flat.objects.filter(
            owner=owner.name,
            owner_pure_phone=owner.pure_phone)
        owner.flats.set(owner_flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20240406_2236'),
    ]

    operations = [
        migrations.RunPython(connect_flats_to_owners),
    ]
