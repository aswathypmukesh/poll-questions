from django import forms
from .models import *


class QuestForm(forms.ModelForm):

    class Meta:
        model = Quest
        fields = "__all__"

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = "__all__"