from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.
def pagProductos(request):
    return render(request, 'productos.html')

def infoCategorias(request, categoria):
    array = Producto.objects.all()
    print((categoria))

    return render(request, 'infoCategorias.html', {
        "categoria":categoria,
        "error":"perro",
        "arreglo":array
    })

def consultaP(request, id):
    array=Producto.objects.filter(ID=id).all()
    return render(request, 'consultaP.html',{
        "id":id,
        "arreglo":array
        })

def godmin(request):
    mensajeError = ""
    if request.method == 'POST':
        nombrep = request.POST['nombrep']
        descripcionp = request.POST['descripcionp']
        categoria = request.POST['categoria']
        cantidadp = request.POST['cantidadp']
        imgp1 = request.POST['imgp']
        imgp2 = request.POST['imgp2']
        imgp3 = request.POST['imgp3']
        valor = request.POST['valor']

        nuevoProducto = Producto.objects.create(nombre_prod=nombrep, descripcion_prod=descripcionp,
                                                 categoria=categoria, cantidad_prod=cantidadp,
                                                   img1_prod = imgp1, img2_prod = imgp2, img3_prod = imgp3, valor=valor)
        
    
    return render(request, 'godmin.html', {
        "error":mensajeError
        })

