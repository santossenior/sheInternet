from django.db import models

class SheInternetForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=100)  # What best describes you
    interested = models.CharField(max_length=100)  # Type of support interested in
    about = models.CharField(max_length=100)  # How did you hear about SheInternet

    def __str__(self):
        return self.email