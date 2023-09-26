from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.handle_runtime_request, name="handle_runtime_request"),
    path("target", views.target, name="target"), 
]
