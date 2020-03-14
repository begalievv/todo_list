from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView
from django.views.generic.edit import FormMixin

from .forms import TodoForm
from .models import Todo


class Main(LoginRequiredMixin,FormMixin, View):
    model = Todo
    template_name = "todo/base.html"
    fields = ('todo',)

    def get(self, request):
        todos = Todo.objects.filter(author=request.user)
        form = TodoForm()
        return render(request, "todo/base.html", {"form": form, "todos": todos})

    def post(self, request):
        todos = Todo.objects.all()
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')
        return render(request, "todo/base.html", {"form": form, "todos": todos})

    #
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


def delete_todo(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('/')


def check_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if todo.flag == 0:
        todo.flag = 1
    else:
        todo.flag = 0
    todo.save()
    return redirect('/')


class UpdateTodo(UpdateView):
    model = Todo
    fields = ['todo',]
    template_name = 'todo/update.html'
