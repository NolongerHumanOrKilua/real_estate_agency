# Generated by Django 2.2.24 on 2022-12-07 18:21

from django.db import migrations

def fill_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        flat.owned_by.set(Owner.objects.filter(owner=flat.owner, owners_phonenumber=flat.owners_phonenumber))


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221207_2027'),
    ]

    operations = [
        migrations.RunPython(fill_owners),
    ]
