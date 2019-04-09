from django.shortcuts import render,render_to_response
from .forms import DetectForm
from .ml import machine
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def hompage(request):
    form = DetectForm(request.POST)
    return render(request, 'index.html', {'form': form})


def result(request):
    form=DetectForm(request.POST)
    if form.is_valid():
        x=form.cleaned_data['msg']
        y=machine(x)
    return render_to_response('index.html',{'message':y,'form':form})


