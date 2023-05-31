from django.urls import path
from .views import ListaFornecedorView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView

urlpatterns = [
    path('', ListaFornecedorView.as_view(), name='fornecedor.index'),
    path('novo/', FornecedorCreateView.as_view(), name='fornecedor.novo'),
    path('editar/<int:pk>', FornecedorUpdateView.as_view(), name='fornecedor.editar'),
    path('remover/<int:pk>', FornecedorDeleteView.as_view(), name='fornecedor.remover')
]
