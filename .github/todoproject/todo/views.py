from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import TodoItem
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    
    def get_queryset(self):
        return TodoItem.objects.order_by('completed', '-created_date')

class TodoCreateView(CreateView):
    model = TodoItem
    template_name = 'todo/todo_create.html'
    fields = ['title', 'description', 'due_date']
    success_url = reverse_lazy('todo_list')