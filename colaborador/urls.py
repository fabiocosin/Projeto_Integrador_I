from django.urls import path
from .views import ListaColaboradorView, ColaboradorCreateView, ColaboradorUpdateView, ColaboradorDeleteView

urlpatterns = [
    path('', ListaColaboradorView.as_view(), name='colaborador.index'),
    path('novo/', ColaboradorCreateView.as_view(), name='colaborador.novo'),
    path('editar/<int:pk>', ColaboradorUpdateView.as_view(), name='colaborador.editar'),
    path('remover/<int:pk>', ColaboradorDeleteView.as_view(), name='colaborador.remover')
]
