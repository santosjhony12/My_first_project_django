from django.contrib import admin
from django.urls import include, path
from app_cad_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('app_cad_usuarios.urls')),

    #rota, view responsavel, nome de referencia (html)
    #path('', views.home, name='home'),
    #path('usuarios/', views.create_usuario, name='listagem_usuarios'),
    #path('deletar', views.delete_usuario, name='deletar'),
   # path('get_by_id/', views.get_by_id, name='get_by_id')
]

