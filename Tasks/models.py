from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    STATUS_CHOICES = (
        ('TODO', 'To Do'),
        ('INPROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
