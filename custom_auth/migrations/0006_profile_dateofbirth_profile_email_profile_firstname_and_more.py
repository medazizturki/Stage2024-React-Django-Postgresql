# Generated by Django 5.0.7 on 2024-08-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0005_remove_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dateofbirth',
            field=models.CharField(default='25-11-2000', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='jhon.jhon@gmail.com', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='John', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='John', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(default='000-000-0000', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.CharField(default='choisi une image', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Client', 'Client')], default='Client', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='sexe',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Homme', max_length=10),
        ),
    ]
