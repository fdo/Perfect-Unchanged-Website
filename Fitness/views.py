# Crete your views here.
from django.shortcuts import HttpResponse
from sams.Fitness.models import Reps


def index(request):
    response = HttpResponse()
    response.write("<html><body><center><H1>reps</H1></center><HR>")
    rlst = Reps.objects.all()   # what we have in lst are the names
                                 # of all the people in the database

    for p in rlst:
        link = "%s --%s" % (p.exercise,p.more)
        response.write("%s<br>reps (or minutes) --  %d<hr>" % (link,p.reps)) 
    #name = models.CharField('name', max_length=200)
    #birthday = models.DateField('Birthday')
    #gender = models.CharField(max_length=1, choices=gender_list)
    #email = models.EmailField('Email', blank=True)

    #favoriteURL =models.URLField('myURL', verify_exists=True)
    #text = models.TextField('Desc', max_length=500, blank=True)

    response.write("</body></html>")
    return response
