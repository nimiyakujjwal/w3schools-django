from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# view to load myfirst.html
def member(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context,request))
