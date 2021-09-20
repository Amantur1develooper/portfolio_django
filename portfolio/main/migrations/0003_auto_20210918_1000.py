# Generated by Django 3.2.7 on 2021-09-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_messege_sendmessege_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='sendmessege',
        ),
    ]
