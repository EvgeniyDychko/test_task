from django.db import models

# Create your models here.
class Notice(models.Model):

    title = models.CharField(max_length=150)
    text = models.TextField()
    numbers = models.IntegerField(default=0)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title
    