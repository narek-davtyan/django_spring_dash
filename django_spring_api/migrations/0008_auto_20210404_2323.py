# Generated by Django 3.1.7 on 2021-04-04 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_spring_api', '0007_auto_20210404_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('Man', 'Man'), ('Woman', 'Woman'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say'), ('M', 'Man'), ('W', 'Woman'), ('O', 'Other'), ('P', 'Prefer not to say')], default=None, max_length=17, null=True),
        ),
    ]
