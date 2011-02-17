from django.db import models

class Running(models.Model):
    data = models.CharField('notes', max_length=200)
    minutes = models.IntegerField()
    timeenter = models.DateTimeField('timeenter')    
    
class Weight(models.Model):
    data = models.CharField('notes', max_length=200)
    damage = models.DecimalField(max_digits=4, decimal_places=1)
    timeenter = models.DateTimeField('timeenter')
    
class Reps(models.Model):
    exercise = models.CharField('exercisetype', max_length=60)
    reps = models.IntegerField()
    more = models.CharField('morenotes', max_length=200)
    timeenter = models.DateTimeField('timeenter')

class PoliceReport(models.Model):
    offense = models.CharField('Offense', max_length=60)
    license_number = models.CharField('plates', max_length=10)
    Details = models.TextField('Details', max_length=2048)
    timeenter = models.DateTimeField('timeenter')
    
    
    
    def __str__(self):
         return '%s' % (self.exercise)


#CREATE TABLE running  (runningkey INTEGER PRIMARY KEY,  
#    data TEXT,     
#    minutes double,            
#    timeEnter DATE);
#CREATE TABLE weight   (weightkey INTEGER PRIMARY KEY,   
#    data TEXT,     
#    damage double,             
#    timeEnter DATE);
#CREATE TABLE reps     (repskey INTEGER PRIMARY KEY,     
#    exercise TEXT, 
#    reps double,    
#    more TEXT, 
#    timeEnter DATE);