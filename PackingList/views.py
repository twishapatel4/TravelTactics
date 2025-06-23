from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'packinglist/task_list.html'  # Ensure correct casing

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_content = self.request.GET.get('search-area', '')
        if search_content:
            context['tasks'] = context['tasks'].filter(title__icontains=search_content)

        context['search_area'] = search_content
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'PackingList/task_details.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'desc', 'complete']
    template_name = 'PackingList/task_form.html'
    success_url = reverse_lazy('packinglist:tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'desc', 'complete']
    template_name = 'PackingList/task_form.html'
    success_url = reverse_lazy('packinglist:tasks')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'PackingList/task_confirm_delete.html'
    success_url = reverse_lazy('packinglist:tasks')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
