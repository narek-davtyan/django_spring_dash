# Generated by Django 3.1.7 on 2021-04-06 16:26

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_spring_api', '0009_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default=None, max_length=2, null=True),
        ),
    ]
