# Generated by Django 4.0 on 2021-12-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_name'),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snack',
            new_name='Snacks',
        ),
    ]