from django.shortcuts import render
from django.website import Person, University

def about(request):
    return render(request, 'about.html', {
    },
    )
