from django.db import models

class Thoughts(models.Model):
    title= models.CharField('Title', max_length=60)
    author = models.CharField('Author', max_length=30)
    details = models.TextField('Details', max_length=2048)
    timeenter = models.DateTimeField('TimeEnter')

    def __str__(self):
         return '%s' % (self.exercise)
