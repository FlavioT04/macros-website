from django.shortcuts import render
from django.http import HttpResponse


def food_list(request):
    return render(request, 'macrosweb/food_list.html')