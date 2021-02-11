from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Goal
from .forms import GoalForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def goals(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            user = request.user
            try:
                goal = Goal.objects.get(user=user)
            except:
                goal = Goal(user=user, ideal_height=0, ideal_weight=0, current_weight=0, current_height=0)
                goal.save()
            goal.ideal_height = form.cleaned_data["ideal_height"]
            goal.ideal_weight = form.cleaned_data["ideal_weight"]
            goal.current_height = form.cleaned_data["current_height"]
            goal.current_weight = form.cleaned_data["current_weight"]
            goal.save()

    user = request.user
    try:
        goal = Goal.objects.get(user=user)
    except:
        goal = Goal(user=user, ideal_height=0, ideal_weight=0, current_weight=0, current_height=0)
        goal.save()
    context = {"ideal_height": goal.ideal_height, 
                 "ideal_weight": goal.ideal_weight, 
                 "current_height": goal.current_height, 
                 "current_weight": goal.current_weight,
                 "form" : GoalForm()
                 }
    return render(request, "profile/goals.html", context)