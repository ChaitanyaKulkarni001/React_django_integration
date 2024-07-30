from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    img_url = models.URLField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    
    def __str__(self):
        return self.name