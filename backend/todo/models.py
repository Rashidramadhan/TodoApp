from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'todos'