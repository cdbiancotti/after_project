from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('paletas/', views.PaletaListView.as_view(), name='lista_paletas'),
    path('paletas/crear/', views.PaletaCreateView.as_view(), name='crear_paleta'),
    path('paletas/<int:pk>/', views.PaletaDetailView.as_view(), name='detalle_paleta'),
    path('paletas/<int:pk>/modificar/', views.PaletaUpdateView.as_view(), name='modificar_paleta'),
    path('paletas/<int:pk>/eliminar/', views.PaletaDeleteView.as_view(), name='eliminar_paleta'),
]
