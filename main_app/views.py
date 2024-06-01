from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FinchForm

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

class FinchListView(ListView):
    model = Finch
    template_name = 'finches/index.html'
    context_object_name = 'finches'

class FinchDetailView(DetailView):
    model = Finch
    template_name = 'finches/detail.html'

class FinchCreateView(CreateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finches/finch_form.html'
    success_url = reverse_lazy('index')

class FinchUpdateView(UpdateView):
    model = Finch
    form_class = FinchForm
    template_name = 'finches/finch_form.html'
    success_url = reverse_lazy('index')

class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'finches/finch_confirm_delete.html'
    success_url = reverse_lazy('index')
