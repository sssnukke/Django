from django.urls import path
from django.views.generic import detail

from .views import TestPageView, about

urlpatterns = [
    path('', TestPageView.as_view(), name='index'),
    path('kt/', about.as_view(), name='tyty'),
]