# Generated by Django 3.2.7 on 2021-09-18 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendmessege',
            old_name='messege',
            new_name='message',
        ),
    ]