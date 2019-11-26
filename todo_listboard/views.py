from django.shortcuts import render
from .models import TodoList
#from .forms import TodoForm
# Create your views here.

from django.views import View
from django.views import generic

class Todo_listBoard(generic.TemplateView):
    def get(self, request, *args, **kwargs):

        template_name = 'todo_board/todo_list.html'
        todo_list = TodoList.objects.all()

        return render(request, template_name, {"todo_list": todo_list})