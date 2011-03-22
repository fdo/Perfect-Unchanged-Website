from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from datetime import datetime
from django import forms
from mydjango.Fitness.models import PoliceReport
from django.template import Context, Template, RequestContext

class EmailForm(forms.Form):
    title = forms.CharField(max_length=50)
    sender = forms.EmailField()
    date = forms.DateTimeField()
    text = forms.CharField(max_length=200)

class PoliceForm(forms.Form):
    offense = forms.CharField(max_length=60)
    license_number = forms.CharField(max_length=10)
    Details = forms.CharField(widget=forms.Textarea(attrs={'rows':'10','cols':'110'}))

class LookyForm(forms.Form):
    offense = forms.CharField(max_length=60)
    license_number = forms.CharField(max_length=10)

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('home/contact_form.html', {'eForm':eForm})

def police(request):
    rForm = PoliceForm()
    if request.method == 'GET':
        message = 'Please add your observations to our database. Thanks for reporting.'
    if request.method == 'POST':
        if request.POST['submit'] == 'Add':
            rf = PoliceForm(request.POST.copy())
            if rf.is_valid():
                try:
                    report=PoliceReport()
                    report.offense = rf.cleaned_data['offense']
                    report.Details = rf.cleaned_data['Details']
                    report.timeenter = datetime.now()
                    report.license_number = rf.cleaned_data['license_number']
                    report.save()
                    goofynumber = report.id + 474244
                    message = 'Thank you for reporting this. The entry number for this incident is %s ' % goofynumber
                except:
                    message = 'Database error %s' % rf.is_valid()
            else:
                message = 'Invalid data in Form'
    return render_to_response('home/police_form.html', {'rForm':rForm, 'message':message}, context_instance=RequestContext(request))

def looky(request):
    lForm = LookyForm()
    if request.method == 'GET':
        message = 'Exactly what kind of reports do you want to look at?'
    if request.method == 'POST':
        if request.POST['submit'] == 'Find It':
            lf = LookyForm(request.POST.copy())
            if lf.is_valid():
                try:
                    report=PoliceReport()
# do a object.all on the police report table 
# and do a select on offense and or license number
                    lookyoffense = lf.cleaned_data['offense']
                    lookylicense_number = lf.cleaned_data['license_number']
                    message = 'Here is the data you asked for. %s' % lookylicense_number
                except:
                    message = 'Database error %s' % lf.is_valid()
            else:
                message = 'Invalid data in Form'
    return render_to_response('home/looky_form.html', {'lForm':lForm, 'message':message}, context_instance=RequestContext(request))
