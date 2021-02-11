from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Goal, Energy
from .forms import GoalForm, EnergyForm
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import io
from statistics import mean


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '/registration/signup.html'

def prepDataAndPlot(energy):
    data = []

    for item in energy:
        temp = []
        temp.append(item.day_date)
        temp.append(item.calorie_intake)
        temp.append(item.calorie_burnt)
        temp.append(item.hours_slept)
        temp.append(item.heart_rate)
        data.append(temp)

    dates = []
    calorie_intake = []
    calorie_burnt = []
    heart_rate = []
    hours_slept = []
    data.sort()

    for i in range(len(data)):
        dates.append(i)
        calorie_intake.append(data[i][1])
        calorie_burnt.append(data[i][2])
        hours_slept.append(data[i][3])
        heart_rate.append(data[i][4])

    fig = plt.figure()
    plt.plot(dates, calorie_intake, label ='Intake') 
    plt.plot(dates, calorie_burnt, label ='Burnt')
    plt.title("Understanding Your Calories")  # add title  
    plt.legend() 
  
    imgdata = io.StringIO()
    fig.savefig(imgdata, format="svg")
    imgdata.seek(0)
    calorie_data = imgdata.getvalue()

    fig = plt.figure()
    plt.plot(dates, hours_slept, label="Hours Slept") 
    plt.title("Understanding Your Sleep Cycle")  # add title  
    plt.legend() 
  
    imgdata = io.StringIO()
    fig.savefig(imgdata, format="svg")
    imgdata.seek(0)
    sleep_data = imgdata.getvalue()

    fig = plt.figure()
    plt.plot(dates, heart_rate, label="Heart Beats Per Minute") 
    plt.title("Understanding your Heart Rate")  # add title  
    plt.legend() 
  
    imgdata = io.StringIO()
    fig.savefig(imgdata, format="svg")
    imgdata.seek(0)
    heart_data = imgdata.getvalue()

    return calorie_burnt, calorie_intake, calorie_data, hours_slept, sleep_data, heart_rate, heart_data


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
        energy = Energy.objects.filter(user=user)
    except:
        energy = []

    calorie_burnt, calorie_intake, calorie_data, hours_slept, sleep_data, heart_rate, heart_data = prepDataAndPlot(energy)

    context = {
                 "form" : EnergyForm(),
                 "calorie_graph": calorie_data,
                 "sleep_graph": sleep_data,
                 "heart_graph": heart_data,
                 "intake_data": mean(calorie_intake),
                 "burnt_data": mean(calorie_burnt),
                 "sleep_data": mean(hours_slept),
                 "heart_data": mean(heart_rate)
                }

    
    return render(request, "profile/energy_analysis.html", context)

def workout(request):
    pass