from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rota, view responsavel, nome de referencia (html)
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('deletar', views.delete_usuario, name='deletar')
]
