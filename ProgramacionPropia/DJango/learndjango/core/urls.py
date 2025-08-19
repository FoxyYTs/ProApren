
from django.urls import path
from .views import my_view, author_view, my_author



urlpatterns = [
    path('listado/', my_view),
    path('detalle/<int:id>', my_author),
    path('marcas/<str:brand>', my_author),
    path('autor/<int:id>', author_view),
]