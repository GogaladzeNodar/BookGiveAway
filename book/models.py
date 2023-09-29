from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

#what models do we need?
# Model Book with fields:  title, owner -> User, author, genrs, description, location
# Model Request with fields: book -> Book, requester-> User, is_accepted - tu True mashin achuqa
#

class Book(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    genrs = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self): 
        return self.title


class Request(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='requested_books', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='owned_books', on_delete= models.CASCADE)
    status = models.CharField(max_length=20, null=True, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'rejected'),

    ])

