# Generated by Django 3.1.7 on 2021-04-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_spring_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
