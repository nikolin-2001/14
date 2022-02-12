from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Yasherka, Pashalkaone, Pashalkatwo
from django.views.generic.edit import CreateView

def index(request):
    merop = Yasherka.objects.order_by('-id')
    context = {'merop': merop}
    return render(request, 'myapi/index.html', context)

class YasherkaViewSet(viewsets.ModelViewSet):
    queryset = Yasherka.objects.all().order_by('name')

class PashalkaoneCreate(CreateView):
    model = Pashalkaone
    fields = ['text']
    def form_valid(self, form):
        self.object = form.save()
        return render(request, 'myapi/Pashalkaone.html', context)

class PashalkatwoCreate(CreateView):
    model = Pashalkatwo
    fields = ['text']
    def form_valid(self, form):
        self.object = form.save()
        return render(request, 'myapi/Pashalkaone.html', context)
