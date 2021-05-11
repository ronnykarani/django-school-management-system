from django.urls import path
#from .views import SignUpView
from .views import profile, update_profile
from accounts import views as user_views


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', user_views.register, name= 'register'),
    path('profile/', profile, name='profile'),
    path('update/', update_profile, name='update-profile')
]

