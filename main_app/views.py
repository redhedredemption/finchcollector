from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Finch, Feeding, Toy
from .forms import FinchForm, FeedingForm, ToyForm

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
        context['toys'] = Toy.objects.all()
        context['toy_form'] = ToyForm()
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

class ToyListView(ListView):
    model = Toy
    template_name = 'toys/index.html'
    context_object_name = 'toys'

class ToyCreateView(CreateView):
    model = Toy
    form_class = ToyForm
    template_name = 'toys/toy_form.html'
    success_url = reverse_lazy('toys_index')

def associate_toy(request, finch_id, toy_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    toy = get_object_or_404(Toy, pk=toy_id)
    finch.toys.add(toy)
    return redirect('detail', pk=finch_id)

def unassoc_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.unassociate(toy_id)
  return redirect('detail', cat_id=cat_id)
