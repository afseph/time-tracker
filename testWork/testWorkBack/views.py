# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Task
from .form import TaskForm

def task_list(request):
    tasks = Task.objects.all().filter(session_id=request.session.session_key)
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    session = request.session.session_key
    print(request.session)
    if request.method == 'POST':
        print(request.POST)
        # print("Session:" + session)
        Task.objects.create(name=request.POST.get("name"), time_elapsed = request.POST.get("time"), session_id=session)
    return JsonResponse({"success":"true"})