from django.shortcuts import render, redirect
from .models import Plan

def pagTienda(request):
    return render(request,'tienda.html')

def pagPlan(request, tipo):
    if tipo == "Todo":
        plan = Plan.objects.all()
    else:
        plan = Plan.objects.filter(TIPO=tipo).all()

    return render(request,'plan.html',{
        "tipo":tipo,
        "plan":plan
        })

def pagContrato(request, id):
    plan=Plan.objects.filter(ID=id).all()
    return render(request,'contrato.html',{
        "id":id,
        "plan":plan
        })

def pagGestor(request):
    plan=Plan.objects.all()

    return render(request,'gestor.html',{
        "plan":plan
        })

def delet(request,id):
    plan = Plan.objects.get(ID = id)
    plan.delete()
    return redirect('/Gestion')

def add(request):
    if request.method == 'POST':
        nombre = request.POST['nameP']
        tipo = request.POST['type']
        desc = request.POST['desc']
        precio = request.POST['value']
        Plan.objects.create(
            NOMBRE = nombre,
            TIPO = tipo,
            DESCRIPCION = desc,
            PRECIO = precio
            )
        
    return redirect('/Gestion')