from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
from .forms import TodoForm

def index_view(request):
    context = {}
    context['todos'] = Todo.objects.all()
    if request.POST:
        form = TodoForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form'] = form
    else:
        form = TodoForm()
        context['form'] = form       
    return render(request, 'index.html', context)
    
