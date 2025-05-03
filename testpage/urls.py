from django.urls import path
from django.views.generic import detail

from .views import index, tyty

urlpatterns = [
    path('', index, name='index'),
    path('kt/', tyty, name='tyty'),
]