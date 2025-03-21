from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure emails are unique

    def __str__(self):
        return self.email