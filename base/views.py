from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project


class ProjectView(DetailView):
    model = Project
    template_name = 'base/single-project.html'

    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(
    #         tags=self.object.tags.all(),
    #         **kwargs
    #     )


class ProjectCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Project
    template_name = 'base/create-project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('projects')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'base/update-project.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy('project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'base/delete-project.html'
    success_url = reverse_lazy('projects')
