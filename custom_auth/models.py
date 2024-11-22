from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title


class Profile(models.Model):
    SEXE_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default="John")
    lastname = models.CharField(max_length=30, default="John")
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='Homme')
    dateofbirth = models.CharField(max_length=30, default="25-11-2000")
    phonenumber = models.CharField(max_length=15, default="000-000-0000")
    email = models.CharField(max_length=30, default="jhon.jhon@gmail.com")
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Client', 'Client')], default='Client')

    def __str__(self):
        return self.user.username

