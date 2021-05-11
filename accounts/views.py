from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, you can now Login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    profile = Profile.objects.filter(id=request.user.id).first()
    context = {
        'profile': profile
    }
    return render(request, 'registration/profile.html', context)


def update_profile(request):
    profile = Profile.objects.filter(id=request.user.id).first()
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms = forms.save(commit=False)
            forms.user = request.user
            forms.save()
            messages.success(request, f'Account updated!')
            return redirect('profile')
    context = {
        'forms': forms
    }
    return render(request, 'registration/update-profile.html', context)
