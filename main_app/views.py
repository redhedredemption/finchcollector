from django.shortcuts import render, get_object_or_404
from .models import Finch

# Import the Finch Model
from .models import Finch



# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')


# Define the about view
def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

# Define index view
def finches_index(request):
  # We pass data to a template very much like we did in Express!
  finches=Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

# Define the detail view
def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})
