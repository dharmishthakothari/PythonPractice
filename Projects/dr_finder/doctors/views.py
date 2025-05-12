from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Doctor
def doctors(request):
    #return HttpResponse("Hello World!!!")
    #mydoctors = Doctor.objects.all().values()
    data = Doctor.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        data=Doctor.objects.filter(Q(firstname__icontains=q)|Q(lastname__icontains=q)|Q(speciality__icontains=q))
    else:
        data = Doctor.objects.all()
    #return render(request,"all_doctors.html",{'data':data})
    template = loader.get_template("all_doctors.html")
    context = {
        'data' : data,
    }
    return HttpResponse(template.render(context,request))
    