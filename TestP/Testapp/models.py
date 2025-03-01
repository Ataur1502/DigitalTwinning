from django.db import models

class Experiment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('yet to begin', 'yet to begin'),
    ]

    roll_no = models.CharField(max_length=20)
    experiment_name = models.CharField(max_length=100)
    assigned_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.roll_no} - {self.experiment_name} ({self.status})"
