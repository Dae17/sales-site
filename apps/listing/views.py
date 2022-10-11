import operator
from django.shortcuts import render
from django.http import HttpResponse

from .models import item

from django.views.generic.edit import CreateView




def index(request):
    objs = item.objects.all()
    ordered = sorted(objs, key=operator.attrgetter('price'))
    # return render(request, 'polls/index.html', {"items":  orderer_item})
    return render(request, 'listing/index.html', {"items": ordered})

def detail(request, id):
    obj = item.objects.get(pk=id)
    return HttpResponse(obj.item_name)

class ItemCreateView(CreateView):
    model = item
    fields = ['item_name', 'price', 'item_discription']
    template_name = 'listing/create.html'

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.owner = self.request.user
        listing.save()
        return super().form_valid(form)