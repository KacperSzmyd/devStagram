from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import UserSignupForm
from .models import Profile
from django.views.generic import ListView, DetailView, CreateView


class ProfileListView(ListView):
    model = Profile
    template_name = 'users/profiles.html'


class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_skills'] = self.object.skill_set.exclude(description__exact="")
        context['other_skills'] = self.object.skill_set.filter(description__exact="")
        return context


class SignUpView(CreateView):
    form_class = UserSignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('profiles')
    success_message = 'Your profile was created successfully'


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Login or password does not match ')


    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logout!')
    return redirect('login')
