from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,TemplateView
# Create your views here.
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

class TutorListView(ListView):
    context_object_name = 'tutors'
    model = models.Tutor

class TutorDetailView(DetailView):
    context_object_name = 'tutor_details'
    model = models.Tutor
    template_name = 'app/tutor_detail.html'
