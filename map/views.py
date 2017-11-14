from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MapMain(TemplateView):
    def get_context_data(self, *args, **kwargs):
        """
            Если мы получили GET запрос.
        """
        context = super(MapMain, self).get_context_data(**kwargs)
        return context
