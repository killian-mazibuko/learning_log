from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

