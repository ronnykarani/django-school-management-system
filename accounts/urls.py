from django.urls import path
#from .views import SignUpView
from .views import profile
from accounts import views as user_views


urlpatterns = [
    path('register/', user_views.register, name= 'register'),
    path('profile/', profile, name='profile'),
]

