from django.shortcuts import render,redirect
from .models import Usuarios

def pagInicio(request):
    return render(request,'index.html')

def pagLogin(request):
    mssgError = ""
    if request.method =='POST':
        usuario = request.POST['user']
        clave = request.POST['pssw']
        try:
            usuarioDB = Usuarios.objects.get(USUARIO = usuario)
            if usuarioDB.CLAVE == clave:
                return redirect('/Tienda')
            else:
                mssgError = "Contraseña incorrecta"
        except:
            mssgError = "El usuario no existe"
    
    return render(request,'login.html',{
        "mssgError":mssgError
        })

def pagRegistro(request):
    mssgError = ""
    if request.method =='POST':
        nombre = request.POST['name']
        apellido = request.POST['lastname']
        usuario = request.POST['user']
        correo = request.POST['email']
        clave = request.POST['pssw']

        try:
            usuarioDB = Usuarios.objects.get(USUARIO = usuario)
            mssgError = "El usuario ya existe"
        except:
            usuarioNuevo = Usuarios.objects.create(
                NOMBRE = nombre,
                APELLIDO = apellido, 
                USUARIO = usuario, 
                CORREO = correo, 
                CLAVE = clave
                )
            return redirect('/Login')
    
    return render(request,'registro.html',{
        "mssgError":mssgError
        })