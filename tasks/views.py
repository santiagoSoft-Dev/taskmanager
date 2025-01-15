from django.shortcuts import render, redirect
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)  

    if request.method == "POST": 
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()  
        return redirect('/tasks/') 

    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
