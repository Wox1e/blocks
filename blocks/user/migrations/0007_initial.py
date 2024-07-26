# Generated by Django 5.0.7 on 2024-07-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0006_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='Никнейм')),
                ('image', models.ImageField(upload_to='user/', verbose_name='Фотография')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
