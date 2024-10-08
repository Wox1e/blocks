# Generated by Django 5.0.7 on 2024-07-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(upload_to='user/avatars', verbose_name='Аватар'),
        ),
    ]
