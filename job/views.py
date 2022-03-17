from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects.all()
    print(jobs[0].summary)
    return render(request, 'home.html', {'jobs': jobs})
