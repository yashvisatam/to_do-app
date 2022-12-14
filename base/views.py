from django.shortcuts import render, redirect
from .models import Tasks
from .forms import AddForm, EditForm
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def home(request):   
    return render(request, 'base/home.html')

def tasksToDo(request):
    tasks = Tasks.objects.all()
    return render(request, 'base/tasks.html', {'tasks':tasks})

def add(request):
    form = AddForm()
    tasks = Tasks.objects.all()
    if request.method == 'POST':
        tasks = Tasks.objects.all()
        Tasks.objects.create(
            tasks = request.POST.get('tasks'),
        )
        return redirect('tasks')
    context = {'form': form, 'tasks': tasks}     
    return render(request, 'base/add.html' , context)

def deleteTask(request, pk):
    tasks = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('tasks')
    return render(request, 'base/delete.html', {'obj': tasks})

def editTask(request, pk):
    tasks = Tasks.objects.get(id=pk)   
    form = EditForm(instance=tasks)
    if request.method == 'POST': 
        form = EditForm(request.POST, instance=tasks)
        tasks = request.POST.get('tasks')
        form.save()
        return redirect('tasks')      
    return render(request, 'base/edit.html', {'form': form, 'tasks': tasks})

@api_view(['GET'])
def taskList(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
   
@api_view(['GET'])
def taskDetail(request,pk):
    task = Tasks.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Tasks.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return Response('Task deleted Successfully!!!')    