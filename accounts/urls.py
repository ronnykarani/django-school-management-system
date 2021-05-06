from django.urls import path
from .views import SignUpView
from django.urls import path
from .views import profile, update_profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('update/', update_profile, name='update-profile')
]
