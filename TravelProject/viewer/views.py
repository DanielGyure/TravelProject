import random
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render
from viewer.models import Travel, Country, City, Profile, Booking
from django.urls import reverse_lazy
from viewer.forms import RegisterUserForm, BookTravelForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail

# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'welcome.html'
    def get_context_data(self, **kwargs):
        travels = Travel.objects.all()[:3]
        context = {"travel1":travels[0], "travel2":travels[1], "travel3":travels[2] }
        return context

class TravelListView(ListView):
    template_name = 'travels.html'
    model = Travel
    context_object_name = 'travels'

    def get_queryset(self):
        travels = Travel.objects.all()

        search = self.request.GET.get('search')

        if search:
            travels_filtered = travels.filter(name__contains=search)
            return travels_filtered

        else:
            return travels

class TravelDetailView(DetailView):
    template_name = 'travel_detail.html'
    model = Travel
    context_object_name = 'travel'

class CreateTravelView(PermissionRequiredMixin, CreateView):
    template_name = 'create_travel.html'
    model = Travel
    fields = '__all__'
    success_url = reverse_lazy('travels')
    permission_required = 'viewer.add_travel'

class UpdateTravelView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_travel.html'
    model = Travel
    fields = '__all__'
    success_url = reverse_lazy('travels')
    context_object_name = 'travel'
    permission_required = 'viewer.change_travel'

class DeleteTravel(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_travel.html'
    model = Travel
    context_object_name = 'travel'
    success_url = reverse_lazy('travels')
    permission_required = 'viewer.delete_travel'

class CountryListView(ListView):
    template_name = 'countries.html'
    model = Country
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    template_name = 'country_detail.html'
    model = Country
    context_object_name = 'country'

class CreateCountryView(PermissionRequiredMixin, CreateView):
    template_name = 'create_country.html'
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.add_country'

class UpdateCountryView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_country.html'
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    context_object_name = 'country'
    permission_required = 'viewer.update_country'

class DeleteCountry(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_country.html'
    model = Country
    context_object_name = 'country'
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.delete_country'

class CityListView(ListView):
    template_name = 'cities.html'
    model = City
    context_object_name = 'cities'

class CityDetailView(DetailView):
    template_name = 'city_detail.html'
    model = City
    context_object_name = 'city'

class CreateCityView(PermissionRequiredMixin, CreateView):
    template_name = 'create_city.html'
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities')
    permission_required = 'viewer.add_city'

class UpdateCityView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_city.html'
    model = City
    fields = '__all__'
    context_object_name = 'city'
    success_url = reverse_lazy('cities')
    permission_required = 'viewer.change_city'

class DeleteCityView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_city.html'
    model = City
    context_object_name = 'city'
    success_url = reverse_lazy('cities')
    permission_required = 'viewer.delete_city'

class RegisterUser(CreateView):
    template_name = 'register_user.html'
    success_url = reverse_lazy('travels')
    form_class = RegisterUserForm

class BookTravel(LoginRequiredMixin, FormView):
    template_name = 'book_travel.html'
    success_url = reverse_lazy('user_booking')
    form_class = BookTravelForm

    def get_initial(self):
        initial = super(BookTravel, self).get_initial()
        travel = Travel.objects.get(id=self.kwargs['pk'])
        profile = Profile.objects.get(user= self.request.user)

        initial.update({'travel': travel.pk, 'profile': profile})
        return initial

    def form_valid(self, form):
        form.save()
        return super(BookTravel, self).form_valid(form)

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('travels')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        print(cleaned_data)

        send_mail(
            f'Contact email from {cleaned_data["name"]}',
            cleaned_data['message'] + f' User email: {cleaned_data["email"]}',
            'contact@nordictravel.com',
            ['daniel.gyure84@gmail.com'],
            fail_silently=False,
        )
        return render(self.request, 'contact_success.html')

class BookingListView(PermissionRequiredMixin, ListView):
    template_name = 'bookings.html'
    model = Booking
    context_object_name = 'bookings'
    permission_required = 'viewer.bookings'

class UserBookingListView(LoginRequiredMixin,ListView):
    template_name = 'user_booking.html'
    model = Booking
    context_object_name = 'bookings'
    permission_required = 'viewer.user_booking'


    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        bookings = Booking.objects.filter(profile=profile)

        return bookings