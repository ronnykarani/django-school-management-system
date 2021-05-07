from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def profile(request):
    profile = UserProfile.objects.filter(id=request.user.id).first()
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)

def update_profile(request):
    profile = UserProfile.objects.filter(id=request.user.id).first()
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms = forms.save(commit=False)
            forms.user = request.user
            forms.save()
            #messages.success(request, f'Account updated!')
            return redirect('profile')
    context = {
        'forms': forms
    }
    return render(request, 'accounts/update-profile.html', context)
