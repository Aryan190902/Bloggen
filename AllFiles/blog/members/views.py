from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from myblog.models import Profile
from .forms import EditProfileForm, ProfilePageForm, SignUpForm, PassChangeForm
from django.views.generic import DetailView, CreateView

class UserRegistration(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PassChangeView(PasswordChangeView):
    form_class = PassChangeForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(**kwargs)
        current_user =  get_object_or_404(Profile, id=self.kwargs['pk'])
        context["current_user"] = current_user
        return context

class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    #fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'linkedin_url',
    #'github_url', 'twitter_url', 'pinterest_url']
    form_class = ProfilePageForm
    # def get_object(self):
    #     return self.request.user

class CreateProfilePage(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)