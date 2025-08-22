
from django.urls import path
from .views import my_view, my_test_view, author_view, CarListView



urlpatterns = [
    path('/listado', my_view),
    path('/detalle/<int:id>', my_test_view),
    path('/marcas/<str:brand>', my_test_view),
    path('/autor/<int:id>', author_view),
    path('/clist', CarListView.as_view()),
]