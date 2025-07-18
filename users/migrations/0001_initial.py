# Generated by Django 5.2.3 on 2025-07-16 07:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('te', 'Telugu'), ('hi', 'Hindi'), ('ta', 'Tamil'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('fr', 'French'), ('de', 'German'), ('es', 'Spanish'), ('it', 'Italian')], default='en', max_length=10)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Help Content',
                'verbose_name_plural': 'Help Contents',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', max_length=10)),
                ('language', models.CharField(choices=[('en', 'English'), ('te', 'Telugu'), ('hi', 'Hindi'), ('ta', 'Tamil'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('fr', 'French'), ('de', 'German'), ('es', 'Spanish'), ('it', 'Italian')], default='en', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Settings',
                'verbose_name_plural': 'User Settings',
            },
        ),
    ]
