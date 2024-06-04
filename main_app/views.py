from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Finch, Feeding
from .forms import FinchForm, FeedingForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feeding_form'] = FeedingForm()
        return context

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

def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = pk
        new_feeding.save()
    return redirect('detail', pk=pk)