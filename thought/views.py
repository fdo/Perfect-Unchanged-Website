from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from datetime import datetime
from django import forms
from mydjango.thought.models import Thoughts
from django.template import Context, Template, RequestContext
from mydjango.settings import STATIC_WEBPAGE_ROOT
from mydjango.settings import STATIC_URL

class ThoughtForm(forms.Form):
    title = forms.CharField(max_length=60)
    author = forms.CharField(max_length=30)
    details = forms.CharField(widget=forms.Textarea(attrs={'rows':'10','cols':'110'}))

def thought(request):
    rForm = ThoughtForm()
    if request.method == 'GET':
        message = 'Please add your observations to our database. Thanks for writing.'
    if request.method == 'POST':
        if request.POST['submit'] == 'Add':
            rf = ThoughtForm(request.POST.copy())
            if rf.is_valid():
                try:
                    report=Thoughts()
                    report.title = rf.cleaned_data['title']
                    report.details = rf.cleaned_data['details']
                    report.timeenter = datetime.now()
                    report.author = rf.cleaned_data['author']
                    report.save()
                    goofynumber = report.id + 474244
                    newfile = STATIC_WEBPAGE_ROOT + 'think/' + report.author + '-' +str(report.id) + '.html'
                    newurl = STATIC_URL + 'think/' + report.author + '-' + str(report.id) + '.html'
                    message = 'Thanks! You created a webpage at %s' % newurl
                    f = open(newfile,'w')
                    f.write("<html><body><center><FONT color=#000090 size=6> %s </FONT><FONT color=#000090 size=2> by </FONT>\n" % report.title)
                    f.write("<FONT color=#000090 size=4> %s </FONT></center><HR>\n" % report.author)
                    f.write("<FONT color=#000090 size=3><pre> %s\n " % report.details)
                    #f.write("<br><FONT color=#002080 size=2> static web page root is %s " % newfile)
                    f.close()
                except:
                    message = 'Database error %s' % rf.is_valid()
            else:
                message = 'Invalid data in Form'
    return render_to_response('thought.html', {'rForm':rForm, 'message':message}, context_instance=RequestContext(request))

