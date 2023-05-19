from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from .forms import *


def index(request):
    return render(request, 'index.html')


# Create your views here.
def viewCategory(request):
    category = Category.objects.all()
    if (request.method == "POST"):
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('viewCategory')
    categoryform = CategoryForm()
    view_data = {
        "category": category,
        'form': categoryform
    }

    return render(request, 'viewCategory.html', view_data)


def viewTask(request, id):
    if request.method == "POST":
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('viewTask', id)
    completed_task = Task.objects.filter(owner=id, status=True)
    pending_task = Task.objects.filter(owner=id, status=False)
    view_data = {
        "completed": completed_task,
        "pending": pending_task,
        "form": TaskForm(),
        "id": id
    }

    return render(request, 'viewItems.html', view_data)


def updateCategory(request, id):
    updating_data = Category.objects.get(id=id)
    categoryform = CategoryForm(instance=updating_data)
    if (request.method == "POST"):
        categoryform = CategoryForm(request.POST, instance=updating_data)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('viewCategory')
    return render(request, 'categoryEdit.html', {'forms': categoryform, 'id': id})


def updateTask(request, id):
    updating_data = Task.objects.get(id=id)
    Task.objects.filter(id=id).update(status=not (updating_data.status))
    return redirect('viewCategory')


@api_view(['GET'])
def apiCategory(request):
    category = Category.objects.all()
    category_serialized = CategorySerializer(category, many=True)
    return Response(category_serialized.data)

@api_view(['GET','POST'])
def apiTask(request):
    if request.method == "GET":
        task = Task.objects.all()
        task_serialized = TaskSerializer(task, many=True)
        return Response(task_serialized.data)
    if request.method == "POST":
        task = Task.objects.filter(owner = request.data['id'])
        task_serialized = TaskSerializer(task,many = True)
        return Response(task_serialized.data)