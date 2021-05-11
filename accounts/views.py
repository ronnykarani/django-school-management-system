from django.shortcuts import render, redirect
#from django.urls import reverse_lazy
#from django.views import generic
from .models import UserProfile
from .forms import ProfileForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
'''
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
'''
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
            messages.success(request, f'Account updated!')
            return redirect('profile')
    context = {
        'forms': forms
    }
    return render(request, 'accounts/update-profile.html', context)
