from django.shortcuts import render

# Create your views here.
from django.views import generic

class Todo_mainboard_in_Views(generic.TemplateView):

    def get(self, request, *args, **kwargs):

        template_name = 'todo_mainboard/index.html'

        return render(request, template_name)