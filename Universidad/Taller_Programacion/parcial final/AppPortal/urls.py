"""
URL configuration for AppPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebInicio.views import pagInicio, pagLogin, pagRegistro
from Servicios.views import pagTienda, pagPlan, pagContrato, pagGestor, delet, add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Gestion/', pagGestor),
    path('', pagInicio),
    path('Login/', pagLogin),
    path('Registrar/', pagRegistro),
    path('Tienda/', pagTienda),
    path('Plan/<str:tipo>', pagPlan, name="Plan"),
    path('Contrato/<int:id>/', pagContrato, name="Contrato"),
    path('Gestion/add/', add, name="add"),
    path('Gestion/delet/<id>/', delet, name="delet"),
]
