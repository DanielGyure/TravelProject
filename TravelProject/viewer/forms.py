from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Booking

class RegisterUserForm(UserCreationForm):

    def save(self):
        new_user = super().save()
        new_profile = Profile.objects.create(user=new_user)
        return new_user


class BookTravelForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'profile': forms.HiddenInput(),
            'travel': forms.HiddenInput()
        }