from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(template_name='registration/signup.html'), name='signup'),
    path('profile/goals/', views.goals, name='profile/goals'),
    path('profile/energy_analysis/',views.energy_analysis,name='profile/energy_analysis'),
    path('profile/workout/', views.workout, name='profile/workout'),
]