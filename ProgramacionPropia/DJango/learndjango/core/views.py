from django.shortcuts import render

# Create your views here.
def view_list(request):
    """View to list all cars."""
    car_list = [
        {'title': 'Carro1','description': 'primer_carro' , 'name': 'Toyota', 'year': 2020, 'color': 'Red'},
        {'title': 'Carro2','description': 'segundo_carro' , 'name': 'Honda', 'year': 2021, 'color': 'Blue'},
        {'title': 'Carro3','description': 'tercer_carro' , 'name': 'Ford', 'year': 2022, 'color': 'Green'},
    ]
    context = {'car_list': car_list}
    return render(request, 'core/car_list.html', context)