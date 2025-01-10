from django.shortcuts import render,redirect
from .models import Usuarios

# Create your views here.
def pagInicio(request):
    return render(request, 'index.html')

def pagLogin(request):
    mensajeError = ""
    if request.method == 'POST':
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        
        try:
            usuarioEncontrado = Usuarios.objects.get(USUARIO = usuario)
            if usuarioEncontrado.CLAVE == clave:
                return redirect('/productos/')
            else:
                mensajeError = "Contraseña incorrecta"
        except:
            mensajeError = "El Usuario no se encontro"

    return render(request, 'login.html', {
        "error":mensajeError
        })

def pagRegistro(request):
    mensajeError = ""
    if request.method == 'POST':
        nombre = request.POST['nombre']
        primerApellido = request.POST['papellido']
        segundoApellido = request.POST['sapellido']
        correo = request.POST['correo']
        usuario = request.POST['usuario']
        clave = request.POST['clave']

        try:
            usuarioEncontrado = Usuarios.objects.get(USUARIO = usuario)
            mensajeError = "Este Usuario ya se encuentra en uso"
        except:
            nuevoUsuario = Usuarios.objects.create(NOMBRE=nombre, P_APELLIDO=primerApellido, S_APELLIDO=segundoApellido,CORREO=correo, USUARIO=usuario, CLAVE=clave)
            return redirect('/login') 
        
    
    return render(request, 'Registro.html', {
        "error":mensajeError
        })