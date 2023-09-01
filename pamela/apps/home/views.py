from django.shortcuts import render
from apps.administration.models import HomeSection, HomeFields

# Create your views here.

def home(request):
    sections = HomeSection.objects.all()
    fields = HomeFields.objects.get(id=1)
    context = {"sections": sections,
               "fields": fields}
    return render(request, "home/home.html", context)


def curriculum(request):
    return render(request, 'home/curriculum.html')