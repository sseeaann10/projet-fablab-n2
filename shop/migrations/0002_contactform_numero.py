# Generated by Django 4.1.7 on 2023-03-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='numero',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
