from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView  # CRUD + Detail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Permissions
from nameservice.models import NameServiceModel  # Model
from django.contrib.messages.views import SuccessMessageMixin  # Messages
# Create your views here.


class Home(ListView):
    model = NameServiceModel
    paginate_by = 30  # add pagination on the list


class SkyNSCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = NameServiceModel
    fields = ['name', 'skylink', 'description']
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):  # logged in user is creating NS
        form.instance.user = self.request.user
        return super().form_valid(form)  # parent class will run form_valid

    def get_success_url(self):
        return reverse('nsDetail', args=(self.object.id,))


class SkyNSListView(LoginRequiredMixin, ListView):
    model = NameServiceModel
    paginate_by = 15  # add pagination on the list

    def get_queryset(self):
        return NameServiceModel.objects.filter(user__id=self.request.user.id)


class SkyNSUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = NameServiceModel
    fields = ['name', 'skylink', 'description']
    success_message = "%(name)s was updated successfully"

    def form_valid(self, form):  # logged in user is updating
        form.instance.user = self.request.user
        return super().form_valid(form)  # parent class will run form_valid

    def test_func(self):  # UserPassesTest denies other users from updating others forms
        ns = self.get_object()  # get NS
        if self.request.user == ns.user:  # if logged-in user is creator return true
            return True
        return False

    def get_success_url(self):
        return reverse('nsDetail', args=(self.object.id,))


class SkyNSDetailView(DetailView):
    model = NameServiceModel


class SkyNSDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NameServiceModel

    def test_func(self):  # UserPassesTest denies other users from updating others forms
        ns = self.get_object()  # get NS
        if self.request.user == ns.user:  # if logged-in user is creator return true
            return True
        return False
    
    def get_success_url(self):
        return reverse('nsList')