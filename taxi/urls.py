from django.urls import path

from .views import index, ManufacturerListView, CarListView, DriverListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("drivers/", DriverListView.as_view(), name="driver-list")
]

app_name = "taxi"
