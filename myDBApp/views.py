from django.shortcuts import render
from myDBApp.models import College, Student
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView,DeleteView
# Create your views here.

class Index(TemplateView):
    template_name = 'myDBApp/index.html'

class CollegeList(ListView):
    model = College

class CreateCollege(CreateView):
    model = College
    fields = '__all__'

class CreateStudent(CreateView):
    model = Student
    fields = '__all__'

class CollegeDetail(DetailView):
    model = College
    context_object_name = 'college_detail'
    template_name = 'myDBApp/college_details.html'

class UpdateStudent(UpdateView):
    model = Student
    fields = '__all__'

class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy('myDBApp:list')
