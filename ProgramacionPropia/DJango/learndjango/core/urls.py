
from django.urls import path
from .views import view_list, author_view, my_author



urlpatterns = [
    path('listado/', view_list),
    path('detalle/<int:id>', my_author),
    path('marcas/<str:brand>', my_author),
    path('autor/<int:id>', author_view),
]