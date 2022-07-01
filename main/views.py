from django.shortcuts import redirect, render
from main.forms import TaskForm
from .models import Task
from .forms import TaskForm


def index(request):
    todolist = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'task' : todolist})

def about(request):
    return render(request, 'main/about.html')

def edit(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/edit.html', context)