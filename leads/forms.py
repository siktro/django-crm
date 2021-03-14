from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Lead

# django can automaticly create a form elements based on class attribs
# but without submit btn

User = get_user_model()

# this is a custom manual form
# its not driven by model at all
# fields don't correlate with model (and DB) fields
class LeadForm(forms.Form):
    # by default attribs are required
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

# linked with actual DB modal
# has more functionality than manual form
class LeadModalForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'agent',
            'first_name',
            'last_name',
            'age',
        )

class CustonUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )
        field_classes = {
            'username': UsernameField
        }