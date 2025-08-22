from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from core.models import Author, Profile

def my_view(request):
    car_list = [
        {'title': 'Carro1','description': 'primer_carro' , 'name': 'Toyota', 'year': 2020, 'color': 'Red'},
        {'title': 'Carro2','description': 'segundo_carro' , 'name': 'Honda', 'year': 2021, 'color': 'Blue'},
        {'title': 'Carro3','description': 'tercer_carro' , 'name': 'Ford', 'year': 2022, 'color': 'Green'},
    ]
    contex = {
        "car_list": car_list,
    }
    return render(request, "core/car_list.html", contex)

class CarListView(TemplateView):
    template_name="core/car_list.html"
    
    def get_context_data(self):
        car_list = [
            {'title': 'Carro1','description': 'primer_carro' , 'name': 'Toyota', 'year': 2020, 'color': 'Red'},
            {'title': 'Carro2','description': 'segundo_carro' , 'name': 'Honda', 'year': 2021, 'color': 'Blue'},
            {'title': 'Carro3','description': 'tercer_carro' , 'name': 'Ford', 'year': 2022, 'color': 'Green'},
        ]
        return {
            "car_list": car_list,
        }

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    author = Author.objects.get(id=kwargs['id'])
    profile = Profile.objects.get(Author_id=kwargs['id'])
    return HttpResponse(f"Author: {author.name} - Biografia: {profile.bio} ")