from django.shortcuts import render
from .models import Usuario
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')

def create_usuario(request):
    novo_usuario = Usuario()
    novo_usuario.name_usuario = request.POST.get('nome')
    novo_usuario.age_usuario = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def delete_usuario(request):
    id = request.POST.get('id')
    print(id)
    usuario_delete = get_object_or_404(Usuario, id_usuario=id)
    usuario_delete.delete()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def update_usuario(request):
    id = request.POST.get('id')



