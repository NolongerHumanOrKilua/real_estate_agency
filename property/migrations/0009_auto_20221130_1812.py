# Generated by Django 2.2.24 on 2022-11-30 15:12

from django.db import migrations

def phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_number = flat.owners_phonenumber
        flat.save()

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(owners_phonenumber__contains='+7000'):
        flat.owner_pure_number = " "
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221129_2239'),
    ]

    operations = [
        migrations.RunPython(phone_numbers, move_backward),
    ]
