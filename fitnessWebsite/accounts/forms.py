  
from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Goal

class BasicForm(forms.Form):
    def disable_field(self, field):
        """
        marks field as disabled
        :param field:
        :return:
        """
        self.fields[field].widget.attrs['disabled'] = ""

    def mark_error(self, field, description):
        """
        Marks the given field as errous. The given description is displayed when the form it generated
        :param field: name of the field
        :param description: The error description
        :return:
        """
        self._errors[field] = self.error_class([description])
        del self.cleaned_data[field]

    def clear_errors(self):
        self._errors = {}

def setup_field(field, placeholder=None):
    """
    This configures the given field to play nice with the bootstrap theme. Additionally, you can add
    an additional argument to set a placeholder text on the field.
    :param field:
    :param placeholder:
    :return:
    """
    field.widget.attrs['class'] = 'form-control'
    if placeholder is not None:
        field.widget.attrs['placeholder'] = placeholder

class GoalForm(BasicForm):

    current_height = forms.DecimalField(label='Current Height', min_value=0)
    setup_field(current_height, "Current Height in cm")
    current_weight = forms.DecimalField(label='Current Weight', min_value=0)
    setup_field(current_weight, "Current Weight in kg")
    ideal_height = forms.DecimalField(label='Ideal Height', min_value=0)
    setup_field(ideal_height, "Ideal Height in cm")
    ideal_weight = forms.DecimalField(label='Ideal Weight', min_value=0)
    setup_field(ideal_weight, "Ideal Weight in kg")


class EnergyForm(BasicForm):
    calorie_intake = forms.DecimalField(label='Calories Intake', min_value=0)
    setup_field(calorie_intake, "Calories Eaten Today")
    calorie_burnt = forms.DecimalField(label='Calories Burnt', min_value=0)
    setup_field(calorie_burnt, "Calories Burnt Today")
    heart_rate = forms.DecimalField(label='Resting Heart Rate', min_value=0)
    setup_field(heart_rate, "Average Resting Heart Rate Today")
    hours_slept = forms.DecimalField(label='Hours Slept', min_value=0)
    setup_field(calorie_burnt, "Number of Hours Slept Today")