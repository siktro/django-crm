from django import forms

from leads.models import Agent

class AgentModalForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('user', )