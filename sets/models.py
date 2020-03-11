from django.db import models
from accounts.models import User

# Create your models here.

class Agency(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    info = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.name

class Agent(models.Model):
    identity = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='agents', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    submission_email = models.EmailField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    genres_of_interest = models.TextField(blank=True)
    is_open_to_queries = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





