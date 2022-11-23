import operator
from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q

from .models import item

from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import DeletionMixin

from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView

from django.views.generic import UpdateView

from django.contrib.auth.views import redirect_to_login

from django.shortcuts import redirect



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

#class UpdateItem(UpdateView):


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


class ItemUpdateView(UpdateView ):
    model = item
    template_name = "listing/update.html"
    fields = ['item_name', 'price', 'item_discription', "photo"]


    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.owner == request.user
        return False

    def post(self, request, *args, **kwargs):
        if "confirm_delete" in self.request.POST:
            self.get_object().delete()
            return redirect("apps:listing:list") 
        return super(ItemUpdateView, self).post(
            request, *args, **kwargs)


    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect("apps:listing:list")
        return super(ItemUpdateView, self).dispatch(
            request, *args, **kwargs)
