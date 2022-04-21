from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Booking

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=500, widget=forms.Textarea)

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
            'name': forms.HiddenInput()
        }