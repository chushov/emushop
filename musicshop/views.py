from django.shortcuts import render
from django import views


class BaseView():

    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', )

    @classmethod
    def as_view(cls):
        pass
