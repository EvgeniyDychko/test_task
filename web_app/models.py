from django.db import models
import re

# Create your models here.

class Notice(models.Model):

    title = models.CharField(max_length=150)
    text = models.TextField()
    numbers = models.IntegerField(default=1)
    date = models.DateField(auto_now_add = True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.numbers = len(set(re.findall('\w+', self.text)))
        super(Notice, self).save(*args, **kwargs)


    