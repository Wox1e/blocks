# Generated by Django 5.0.7 on 2024-07-21 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_users_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
