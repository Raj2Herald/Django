from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    duration = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.origin + " " + self.destination