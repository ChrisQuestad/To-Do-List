from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from .models import Task, List
from .forms import TaskForm, ListForm



class HomePageView(View):
    template_name = 'layout.html'

    def get(self, request, *args, **kwargs):
        lists = List.objects.all()

        return render(request, self.template_name, {'lists':lists})


class ListDetailView(DetailView):
    model = List
    template_name = 'lists/detail.html'


class ListUpdateView(View):
    form_class = ListForm
    template_name = 'lists/update.html'

    def get(self, request, *args, **kwargs):
        model = List.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(instance=model)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            return redirect('lists:detail', pk=model.pk)

        return render(request, self.template_name, {'form': form})



class ListDeleteView(View):
    def post(self,request, *args, **kwargs):
        model = List.objects.get(pk=self.kwargs['pk'])
        if request.method =='POST':
            model.delete()
            return redirect('home')



class ListCreateView(View):
    form_class = ListForm
    template_name = 'lists/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            return redirect('lists:detail', pk=model.pk)

        return render(request, self.template_name, {'form': form})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'lists/tasks/detail.html'

    def get_queryset(self):
        return Task.objects.filter(lists__pk=self.kwargs['lists_pk'])

class TaskDeleteView(View):
    def post(self,request, *args, **kwargs):
        model = Task.objects.get(pk=self.kwargs['pk'])
        if request.method =='POST':
            model.delete()
            return redirect('home')

class TaskCreateView(View):
    form_class = TaskForm
    template_name = 'lists/tasks/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        lists = List.objects.get(pk=self.kwargs['list_pk'])



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        model = List.objects.get(pk=self.kwargs['list_pk'])
        if form.is_valid():
            model.lists = lists
            model.save()
            return redirect('lists:tasks-detail', lists_pk=lists.pk, pk=model.pk)

        return render(request, self.template_name, {'form': form})

class TaskUpdateView(View):
    form_class = TaskForm
    template_name = 'tasks/update.html'

    def get(self, request, *args, **kwargs):
        model = Task.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(instance=model)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            return redirect('task:detail', pk=model.pk)

        return render(request, self.template_name, {'form': form})
