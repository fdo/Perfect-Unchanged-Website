from django.shortcuts import HttpResponse
from mydjango.people.models import Person

def index(request):
    response = HttpResponse()
    response.write("<center><H1>People</H1></center><HR>")
    lst = Person.objects.all()   # what we have in lst are the names
                                 # of all the people in the database

    for p in lst:
        link = "<a href=\"Info/%d\">" % p.id
        response.write("<li>%s%s</a></li>" % (link,p.name)) 
    #name = models.CharField('name', max_length=200)
    #birthday = models.DateField('Birthday')
    #gender = models.CharField(max_length=1, choices=gender_list)
    #email = models.EmailField('Email', blank=True)

    #favoriteURL =models.URLField('myURL', verify_exists=True)
    #text = models.TextField('Desc', max_length=500, blank=True)

    response.write("</body></html>")
    return response
    
def colors(request):
    colors = ("BLUE","RED","GREEN")
    response = HttpResponse()
    response.write("<HTML><BODY>\n")
    response.write("<H1>Color Index</H1><HR>\n")
    for c in colors:
        response.write("<FONT COLOR=%s><LI>%s</LI></FONT>\n" % (c,c))
    response.write("</BODY></HTML>")
    return response