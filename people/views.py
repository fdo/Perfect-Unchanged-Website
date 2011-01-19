from django.shortcuts import HttpResponse
from mydjango.people.models import Person

def index(request):
    response = HttpResponse()
    response.write("<center><H1>People</H1></center><HR>\n")
    lst = Person.objects.all()   # what we have in lst are the names
                                 # of all the people in the database
    for p in lst:
        link = "<a href=\"Info/%d/\">\n" % p.id
        response.write("<li>%s%s</a></li>\n" % (link,p.name)) 
    response.write("</body></html>\n")
    return response

def what(request):
    response = HttpResponse()
    response.write("<body><html>\n")
    response.write("<title>database programming is what this is</title>\n")
    response.write("<center><H3>Django code I fiddled up to learn how to access databases from the web</H3></center><HR>\n")
    link = "<a href=\"/people/\">\n"
    response.write("<li>%slist of people</a></li>\n" % link) 
    link = "<a href=\"/fitness/weight/\">\n"
    response.write("<li>%srecordings of my weight</a></li>\n" % link) 
    link = "<a href=\"/fitness/running/\">\n"
    response.write("<li>%sskimpy running diary</a></li>\n" % link) 
    link = "<a href=\"/fitness/reps/\">\n"
    response.write("<li>%sexercise</a></li>\n" % link) 
    link = "<a href=\"/fitness/reps/chinups/\">\n"
    response.write("<li>%schinups</a></li>\n" % link) 
    response.write("<p>Coming soon, forms...<p>\n")
    response.write("<a href="http://fit.gorchs.net/">this code in action</a>")
    response.write("</body></html>\n")
    return response
    
def details(request, pID='0'):
    myname = "everybody"
    response = HttpResponse()
    response.write("<HTML><BODY>\n")
    try:
        p = Person.objects.get(id=pID)
        response.write("<h1>Details for %s</h1><hr>\n" % p.name)
        response.write("<li>Birthday: %s</li>\n" % p.birthday)
        response.write("<li>Email: %s</li>\n" % p.email)
        response.write("<li>URL: %s</li>\n" % p.favoriteURL)
        response.write("<li>Info: %s</li>\n" % p.text)
    except Person.DoesNotExist:
        response.write("Person Not Found")
    response.write("</BODY></HTML>\n")
    return response
    
def colors(request):
    colors = ("BLUE","RED","GREEN")
    response = HttpResponse()
    response.write("<HTML><BODY>\n")
    response.write("<H1>Color Index</H1><HR>\n")
    for c in colors:
        response.write("<FONT COLOR=%s><LI>%s</LI></FONT>\n" % (c,c))
    response.write("</BODY></HTML>\n")
    return response