from django.shortcuts import render
from django.http import HttpResponse

from apps.listing.forms import ListingForm
from .models import item

from django.views.generic.edit import FormView


def index(request):
    objs = item.objects.all()
    return render(request, 'listing/index.html', {"items": objs})

def detail(request, id):
    obj = item.objects.get(pk=id)
    return HttpResponse(obj.item_name)

# https://docs.djangoproject.com/en/4.1/topics/forms/
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/
class create(FormView):
    template_name = 'listing/create.html'
    form_class = ListingForm
    success_url = '/thanks/'

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.owner = self.request.user
        listing.save()
        return super().form_valid(form)