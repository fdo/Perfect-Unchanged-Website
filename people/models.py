from django.db import models
from django.contrib.auth.models  import User

gender_list = (('M','Male'),('F','Female'))
# Create your models here.
class Person(models.Model):
    name = models.CharField('name', max_length=200)
    birthday = models.DateField('Birthday')
    gender = models.CharField(max_length=1, choices=gender_list)
    email = models.EmailField('Email', blank=True)
#    headshot = models.ImageField(upload_to='img', blank=True)
    favoriteURL =models.URLField('myURL', verify_exists=True)
    text = models.TextField('Desc', max_length=500, blank=True)
    def __str__(self):
        return '%s' % (self.name)