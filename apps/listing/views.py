import operator
from django.shortcuts import render
from django.http import HttpResponse

from .models import item

from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView

from django.contrib.messages.views import SuccessMessageMixin



def list(request):
    objs = item.objects.all()
    ordered = sorted(objs, key=operator.attrgetter('price'))
    # return render(request, 'polls/index.html', {"items":  orderer_item})
    return render(request, 'listing/list.html', {"items": ordered})

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
    