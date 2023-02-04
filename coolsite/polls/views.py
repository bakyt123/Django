from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import ItemStore, Category
from django.urls import reverse
from django.utils import timezone


class ViewHome(ListView):
    model = ItemStore
    template_name = 'polls/index.html'


    def get_queryset(self, **kwargs):
        return ItemStore.objects.filter(is_Activ=True)


def CategoryView(request):
    cat = Category.objects.all()
    return render(request, cat=cat)
