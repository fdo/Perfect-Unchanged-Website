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
    Details = forms.CharField(widget=forms.Textarea(attrs={'rows':'4','cols':'40'}))

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('home/contact_form.html', {'eForm':eForm})

def police(request, pID='1'):
    rForm = PoliceForm()
    if request.method == 'GET':
        message = 'Please add your observations to our database, paranoia will destroya. JUST THE FACTS'
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
                    message = 'Thank you for snitching. The entry number for this incident is %s ' % report.id
                except:
                    message = 'Database error %s' % rf.is_valid()
            else:
                message = 'Invalid data in Form'

    return render_to_response('home/police_form.html', {'rForm':rForm, 'message':message}, context_instance=RequestContext(request))
