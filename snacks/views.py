from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name="home.html"
    model=Snack

class SnackDetailView(DetailView):
    template_name="details.html"
    model=Snack

class SnackCreateView(CreateView):
    template_name = 'createSnacks.html'
    model = Snack
    fields=['title','purchaser','description']
    # success_url = reverse_lazy('create')

class SnackUpdateView(UpdateView):
    template_name="updateSnacks.html"
    model=Snack
    fields='__all__'
    success_url = reverse_lazy('home')

class SnackDeleteView(DeleteView):
    template_name="deleteSnacks.html"
    model=Snack
    success_url = reverse_lazy('home')