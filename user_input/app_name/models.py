from django.db import models

class UserInput(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"

# Create your models here.
