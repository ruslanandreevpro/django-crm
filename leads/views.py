from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.

def lead_list(request):
    # return HttpResponse("Hello world")
    leads = Lead.objects.all()

    context = {
        "leads": leads
    }

    return render(request, "leads/lead_list.html", context)

def lead_detail(request, id):
    lead = Lead.objects.get(id=id)
    
    context = {
        "leads": lead
    }

    return render(request, "leads/lead_detail.html", context)