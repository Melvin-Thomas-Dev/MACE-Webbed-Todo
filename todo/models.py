from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=20, blank = False)
    description = models.CharField(max_length= 150, blank=False)

    def __str__(self):
        return self.title