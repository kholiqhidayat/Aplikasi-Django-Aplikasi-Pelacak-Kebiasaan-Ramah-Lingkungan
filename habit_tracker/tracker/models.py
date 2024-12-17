from django.db import models

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    frequency = models.CharField(max_length=50)  # Daily, Weekly, Monthly

    def __str__(self):
        return self.name
