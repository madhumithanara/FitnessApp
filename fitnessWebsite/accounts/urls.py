from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/goals/', views.goals, name='profile/goals'),
    path('profile/calorie_counter',views.calorie_counter,name='profile/calorie_counter'),
]