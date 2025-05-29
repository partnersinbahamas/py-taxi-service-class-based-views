from django.shortcuts import render
from django.views.generic import ListView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    context_object_name = "manufacturers"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related('manufacturer').order_by("model")
    context_object_name = "cars"
    paginate_by = 5
