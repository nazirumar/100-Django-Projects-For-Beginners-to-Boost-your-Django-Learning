
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from todo_app.models import Todo
from todo_app.forms import TodoForm
from django.contrib import messages

# Create your views here.




def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            userform.user = request.user
            userform.save()
            messages.success(request, "New Task Added!")
            return redirect('home')
    todos = Todo.objects.filter(user=request.user).only('title', 'is_reading')
    return render(request, 'home.html', {'todos':todos})
  


def upadateView(request, pk):
    query = get_object_or_404(Todo, pk=pk)
    if not query.is_reading:
        query.is_reading = True
        query.save()
        messages.info(request, f"Task {query.pk} Updated Successfuly!")
        return redirect('home')
    else:
        query.is_reading = False
        query.save()
        messages.info(request, f"Task {query.pk} Updated Successfuly!")

        return redirect('home')


def deleteView(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user == todo.user:
        todo.delete()
        messages.warning(request, f"Task {todo.pk} Deleted Successfuly!")
        return redirect('home')
    else:
        messages.error(request, f"You don't Have Permission to delete this Task {todo.pk}!!")
        return redirect('home')

    
def detailview(request, pk):
    query = get_object_or_404(Todo, pk=pk)
    return render(request,'detail.html', {'query':query})

    


