# Generated by Django 2.2.24 on 2022-12-19 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20221211_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_claim', to='property.Flat', verbose_name='Квартира, на которую жаловались'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_claim', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
