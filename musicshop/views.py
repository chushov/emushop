from django.shortcuts import render
from django import views


class BaseView(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', )
