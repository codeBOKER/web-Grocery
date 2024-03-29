from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.user)
