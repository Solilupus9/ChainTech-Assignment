from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Data
from .forms import Input
import pyquotegen
def main(request):
    quote=pyquotegen.get_quote()
    context={
        'quote':quote,
        'form':Input()
    }
    return render(request,'main.html',context)

class SubmitData(CreateView):
    model = Data
    form_class = Input
    template_name = 'main.html'
    success_url = reverse_lazy('success')

def success(request):
    return render(request,'success.html')

def viewdata(request):
    stored_data=Data.objects.all()
    return render(request,'viewdata.html',{'data':stored_data})
