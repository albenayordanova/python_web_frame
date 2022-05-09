from django.views import generic as view
from django.shortcuts import render

from demo_app.web.models import Item


class IndexView(view.ListView):
    template_name = 'index.html'
    model = Item
