# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from datetime import datetime
from django import forms
from django.forms import ModelForm
from mydjango.Fitness.models import PoliceReport
from django.template import Context, Template, RequestContext

class EmailForm(forms.Form):
    title = forms.CharField(max_length=50)
    sender = forms.EmailField()
    date = forms.DateTimeField()
    text = forms.CharField(max_length=200)

#class PoliceForm(ModelForm):
#    class Meta:
#        model = PoliceReport

class PoliceForm(forms.Form):
    offense = forms.CharField(max_length=60)
    license_number = forms.CharField(max_length=10)
    Details = forms.CharField(widget=forms.Textarea(attrs={'rows':'4','cols':'40'}))
    timeenter = forms.DateTimeField()

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('home/contact_form.html', {'eForm':eForm})

def police(request, pID='1'):
#    c = {}
#    c.update(csrf(request))
    massage = 'Just the Facts'
    report = get_object_or_404(PoliceReport, pk=pID)
    rForm = PoliceForm()
    if request.method == 'GET':
        massage = 'fact: %s' % report.offense

    if request.method == 'POST':
        if request.POST['submit'] == 'Add':
            rf = PoliceForm(request.POST.copy())
            postDict = request.POST.copy()
           # postDict['timeenter'] = datetime.now
            save_rf = PoliceForm(postDict)
            if save_rf.is_valid():
#            if rf.is_valid():
                try:
    #                rObj = save_rf.save()
                    report.offense = save_rf.offense
                    report.Details = save_rf.Details
                    report.timeenter = save_rf.timeenter
                    report.license_number = save_rf.license_number
                    report.save()
                    massage = ' %s - offense added' % report.offense
                except:
                    massage = 'Database error %s' % save_rf.offense
	    else:
		massage = 'Invalid data in Form'

#    return render_to_response("home/police_form.html", c)
#    return render_to_response('home/police_form.html', {'rForm':rForm, 'massage':massage}, c)
#    return render_to_response('home/police_form.html', {'rForm':rForm, 'massage':massage})
    return render_to_response('home/police_form.html', {'rForm':rForm, 'massage':massage}, context_instance=RequestContext(request))

def my_view(request):
   # ... view code here
    return render_to_response("a_template.html", c)
