import operator
from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q

from .models import item

from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import TemplateView, ListView




class ItemDetailView(DetailView):
    model = item


class ItemCreateView(SuccessMessageMixin, CreateView):
    model = item
    fields = ['item_name', 'price', 'item_discription', "photo"]
    template_name = 'listing/create.html'
    success_message = "'%(item_name)s' was created successfully"


    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.owner = self.request.user
        listing.save()
        return super().form_valid(form)


class ListAndSearchView(ListView):
    model = item
    template_name = 'listing/list.html'

    def get_queryset(self):  # new
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                item_name__icontains=query 
            )
        ordered = sorted(queryset, key=operator.attrgetter('price'))
        return ordered