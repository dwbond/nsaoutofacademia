from django.shortcuts import render
from website.models import Person, University

def universities(request):
    universities = University.objects.all()
    return render(request, 'index.html', {
        'universities' : universities,
    },
    )
