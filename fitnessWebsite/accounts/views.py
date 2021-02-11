from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Goal, Energy
from .forms import GoalForm, EnergyForm


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
    goal = None
    try:
        goal = Goal.objects.get(user=user)
    except:
        goal = Goal(user=user, ideal_height=1, ideal_weight=1, current_weight=1, current_height=1)
        goal.save()

    #calculation of bmi: bmi = kg/m^2
    ideal_bmi = round(goal.ideal_weight/((goal.ideal_height/100)**2), 2)
    current_bmi = round(goal.current_weight/((goal.current_height/100)**2), 2)

    context = {"ideal_height": goal.ideal_height, 
                 "ideal_weight": goal.ideal_weight, 
                 "current_height": goal.current_height, 
                 "current_weight": goal.current_weight,
                 "ideal_bmi": ideal_bmi,
                 "current_bmi": current_bmi,
                 "form" : GoalForm()
                 }

    
    return render(request, "profile/goals.html", context)

def energy_analysis(request):
    if request.method == "POST":
        form = EnergyForm(request.POST)
        if form.is_valid():
            user = request.user
            energy = Energy(user=user)
            energy.calorie_intake = form.cleaned_data["calorie_intake"]
            energy.calorie_burnt = form.cleaned_data["calorie_burnt"]
            energy.hours_slept = form.cleaned_data["hours_slept"]
            energy.heart_rate = form.cleaned_data["heart_rate"]
            energy.save()

    user = request.user
    energy = None
    try:
        energy = Energy.objects.get(user=user)
    except:
        energy = None

    context = {}
    # context = {"ideal_height": goal.ideal_height, 
    #              "ideal_weight": goal.ideal_weight, 
    #              "current_height": goal.current_height, 
    #              "current_weight": goal.current_weight,
    #              "ideal_bmi": ideal_bmi,
    #              "current_bmi": current_bmi,
    #              "form" : GoalForm()
    #              }

    
    return render(request, "profile/energy_analysis.html", context)