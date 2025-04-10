from django.db import models

class VolunteerForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    contribution = models.CharField(max_length=100)  # How would you like to contribute
    time_commitment = models.CharField(max_length=100)  # How much time can you commit
    message = models.TextField(blank=True, null=True)  # Optional message

    def __str__(self):
        return self.email