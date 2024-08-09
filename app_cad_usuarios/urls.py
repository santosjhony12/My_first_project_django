from django.urls import path
from app_cad_usuarios import views


urlpatterns = [
    path('get_by_id/', views.get_by_id, name='get_by_id'),
    path('get_all/', views.get_all_users, name='get_all'),
    path('create_user/', views.create_user, name='create_user'),
    path('delete_user/', views.delete_user, name='delete_user')
]


