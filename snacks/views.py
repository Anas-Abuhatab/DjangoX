from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Snacks


class SnacksListView(ListView):
    template_name = "snack/snack-list.html"
    model = Snacks


class SnacksDetailView(DetailView):
    template_name = "snack/snack-detail.html"
    model = Snacks


class SnacksCreateView(CreateView):
    template_name = "snack/snack-create.html"
    model = Snacks
    fields = ['name', 'purchaser', 'description']
    success_url = reverse_lazy("snack_list")


class SnacksUpdateView(UpdateView):
    template_name = "snack/snack-update.html"
    model = Snacks
    fields = ['name', 'purchaser', 'description']
    success_url = reverse_lazy("snack_list")


class SnacksDeleteView(DeleteView):
    template_name = "snack/snack-delete.html"
    model = Snacks
    success_url = reverse_lazy("snack_list")