from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Chirp
from users.models import CustomUser


class ChirpListView(ListView):
    """
    Inherits 'ListView'. View is used to list the Chirps. We can use 'chirp_list' and 'object_list' to get the queryset in the list template.
    """
    model = Chirp
    template_name = 'home.html'


class ChirpDetailView(DetailView):
    """
    Inherits 'DetailView'. View is used to display one Chirp. We can use 'chirp' or 'object' to get the content in detail template.
    """
    model = Chirp
    template_name = 'chirp_detail.html'


class ChirpCreateView(LoginRequiredMixin, CreateView):
    """
    Inherits 'CreateView' and ''. View is used to create a new Chirp.
    """
    model = Chirp
    template_name = 'chirp_hatch.html'
    # Specifies which fields to provide for create view.
    fields = ['tiny_body']
    
    # 'form_valid' runs after the form has been validated but before data is saved to database.
    # Add a field 'author' to form and assigns the value of 'user' of the 'request' to be the value of the 'form' 'instance's 'author'.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# TODO: Separate 'Moderate' and 'Edit' views and HTMLs since functionality should be different.
class ChirpModerateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Inherits 'UpdateView'. View used to edit the content of a Chirp.
    """
    model = Chirp
    template_name = 'chirp_moderate.html'
    # Specifies which fields to provide for update view.
    fields = ['tiny_body']

    # def test_func(self):
    #     """
    #     Returns 'True' if the 'author' of the 'chirp' is the same user as the 'request' 'user'. Otherwise, returns 'False'.
    #     """
    #     # 'get_object()' gets the specific instance of the 'Chirp' which is within the 'request'.
    #     chirp = self.get_object()
    #     print(f"self.request.user: {self.request.user}")
    #     print(f"chirp.author: {chirp.author}")
    #     print(f"Requesting user is Chirp author: {self.request.user == chirp.author}")
    #     # Logged in user: 'self.request.user'
    #     # Author of Chirp: 'chirp.author'
    #     return self.request.user == chirp.author
    
    def test_func(self):
        """
        Returns 'True' if the 'request' 'user' is a moderator OR 'request' 'user' is 'chirp' 'author'. Otherwise, returns 'False'.
        """
        chirp = self.get_object()
        print(f"self.request.user.is_moderator: {self.request.user.is_moderator}")
        return self.request.user.is_moderator or self.request.user == chirp.author


class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Inherits 'DeleteView'. View used to delete a Chirp.
    """
    model = Chirp
    template_name = 'chirp_delete.html'
    # Function view: reverse()
    # Class view: reverse_lazy()
    success_url = reverse_lazy('chirps:home')

    def test_func(self):
        """
        Returns 'True' if the 'request' 'user' is a moderator OR 'request' 'user' is 'chirp' 'author'. Otherwise, returns 'False'.
        """
        chirp = self.get_object()
        print(f"self.request.user: {self.request.user}")
        print(f"chirp.author: {chirp.author}")
        print(f"Requesting user is Chirp author: {self.request.user == chirp.author}")
        return self.request.user.is_moderator or self.request.user == chirp.author   

