from django.shortcuts import render, redirect

from .models import Symptom
from .model.model import predict


def index(request):
    symptoms = Symptom.objects.order_by('id')
    context = {'symptoms': symptoms, 'ids': [i for i in range(1, len(symptoms)+1)]} 
    return render(request, 'diagnosis/index.html', context)

def result(request):
    if request.method == 'POST':
        x = [] # inputs of neural network
        for i in range(1, len(Symptom.objects.all())+1):
            symptom_list = request.POST.getlist('symp%i' %i)
            if symptom_list:
                x.append(1)
            else:
                x.append(0)

        return render(request, 'diagnosis/result.html', {'result': predict(x)})
    else:
        return redirect('diagnosis:index')
        

    