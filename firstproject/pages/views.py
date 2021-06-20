from django.shortcuts import render
from django.views.generic import ListView
from .models import Page

class HomePageView(ListView):
	model=Page
	template_name='home.html'
	context_object_name='all_pages_list'

# Create your views here.
