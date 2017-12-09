from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.detail import DetailView


from .models import Task, List
from .forms import TaskForm, ListForm



class HomePageView(View):
    template_name = 'lists/home.html'

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
        model = List.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('lists:detail', pk=model.pk)

        return render(request, self.template_name, {'form': form})



class ListDeleteView(View):
    def post(self,request, *args, **kwargs):
        model = List.objects.get(pk=self.kwargs['pk'])
        if request.method =='POST':
            model.delete()
            return redirect('lists:home')



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




class TaskDeleteView(View):
    def post(self,request, *args, **kwargs):
        model = Task.objects.get(pk=self.kwargs['pk'])
        model.delete()
        return redirect('lists:detail', pk=self.kwargs['list_pk'])

class TaskCreateView(View):
    form_class = TaskForm
    template_name = 'lists/tasks/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        lists = List.objects.get(pk=self.kwargs['list_pk'])

        return render(request, self.template_name, {'form': form})



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        todo_list = List.objects.get(pk=self.kwargs['list_pk'])
        if form.is_valid():
            model = form.save(commit=False)
            model.todo_list = todo_list
            model.save()
            return redirect('lists:detail', pk=todo_list.pk)

        return render(request, self.template_name, {'form': form})

class TaskUpdateView(View):
    def post(self, request, *args, **kwargs):
        model = Task.objects.get(pk=self.kwargs['pk'])
        model.completed = not model.completed
        model.save()
        return redirect('lists:detail', pk=self.kwargs['list_pk'])
