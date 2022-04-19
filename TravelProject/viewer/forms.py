from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterUserForm(UserCreationForm):

    def save(self):
        new_user = super().save()
        new_profile = Profile.objects.create(user=new_user)
        return new_user