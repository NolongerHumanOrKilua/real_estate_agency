# Generated by Django 2.2.24 on 2022-11-29 14:18

from django.db import migrations

def is_new(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year > 2014
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(is_new),
    ]
