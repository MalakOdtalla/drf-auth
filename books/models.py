from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    year_of_publication = models.TextField()

    def __str__(self):
        return self.name