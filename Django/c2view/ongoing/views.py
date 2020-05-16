from django.utils import timezone
from .models import To_do
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from datetime import datetime
from django.db.models import DurationField, ExpressionWrapper, F, DateTimeField
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models.functions import Now
from c2vconfig.models import MP4


def index(request):
    myDate = datetime.now()
    MP4query = MP4.objects.all()
    days_left1 = To_do.objects.annotate(
        delta1=ExpressionWrapper(F('end') - Now(), output_field=DurationField()))
    return render(request, 'amp/ongoingtest.html', {
        'myDate': myDate,
        'days_left1': days_left1,
        'MP4query': MP4query})


class HomeView(ListView):
    template_name = 'ongoing.html'
    model = To_do
    myDate = datetime.now()

    def get(self, request, *args, **kwargs):
        myDate = datetime.now()
        queryset = self.model.objects.annotate(
            delta1=ExpressionWrapper(F('end') - Now(), output_field=DurationField()))
        return render(request, self.template_name, {
            'myDate': myDate,
            'queryset': queryset,
            })


class DetailView(DetailView):
    model = To_do
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class OngoingCreate(CreateView):
    template_name = 'Ongoingform.html'
    success_url = '/ongoing'
    model = To_do
    fields = ['task', 'topic', 'how', 'end', 'status1']


class OngoingUpdate(UpdateView):
    model = To_do
    template_name = 'Ongoingform.html'
    fields = ['task', 'topic', 'how', 'end', 'status1']
    success_url = '/ongoing'


class OngoingDelete(DeleteView):
    model = To_do
    success_url = reverse_lazy('home2')
