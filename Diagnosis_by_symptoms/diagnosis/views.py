from django.shortcuts import render

from .models import Symptom

def index(request):
    symptoms = Symptom.objects.order_by('id')
    context = {'symptoms': symptoms, 'ids': [i for i in range(1, len(symptoms)+1)]} 
    return render(request, 'diagnosis/index.html', context)