from django import forms
from .models import *


class QuestForm(forms.ModelForm):

    class Meta:
        model = Quest
        fields = "__all__"

