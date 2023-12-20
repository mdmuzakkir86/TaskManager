from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Q


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'Tasks/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'Tasks/task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'Tasks/task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'Tasks/task_delete.html', {'task': task})


def task_search(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(Q(title__icontains=query) | Q(status__icontains=query))
    return render(request, 'Tasks/task_list.html', {'tasks': tasks})
