from django.shortcuts import render
from .models import Usuario
from django.shortcuts import get_object_or_404, redirect
import json
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#@csrf_exempt 
#uso somente em metodos POST/PATCH/PUT/DELETE

def get_all_users(request):
    if request.method == 'GET':
        users = list(Usuario.objects.all().values('name_usuario', 'id_usuario'))
        return JsonResponse({'users': users}, status=200)
    else:
        return JsonResponse({'error': 'Http method incorrect.'})

def get_by_id(request):
    if request.method == 'GET':
        body = json.loads(request.body)
        user_id = body.get('id')
 
        if not user_id:
            return JsonResponse({'error': 'User id cannot be null'})
        try:
            user = get_object_or_404(Usuario, id_usuario=user_id)
            return JsonResponse({'user': user}, status=200)
        except Http404 as e:
            return JsonResponse({'error': 'User does not exist.'}, status=404)
    else:
        return JsonResponse({'error': 'Http method incorrect.'})


@csrf_exempt
def create_user(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Http method incorrected.'})
    try:
        body = json.loads(request.body)
        new_user = Usuario()
        name_user = body.get('name')
        age_user = body.get("age")
        new_user.name_usuario = name_user
        new_user.age_usuario = age_user
        new_user.save()
        return JsonResponse({'Message': 'User has been created'}, status=201)
    except Exception:
        return JsonResponse({'error': "Something is wrong."})

    
@csrf_exempt
def delete_user(request):
    if not request.method == 'DELETE':
        return JsonResponse({'error': 'Http Method incorrected'})
    
    try:
        body = json.loads(request.body)
        user_id = body.get('id')

        response_user = get_object_or_404(Usuario, id_usuario=user_id)
        if not response_user:
            return JsonResponse({'message':'User does not exist'}, status=404)
        
        response_user.delete()
        return JsonResponse({"message": 'User has been deleted'}, status=204)
    except Http404:
        return JsonResponse({"message": 'User does not exist'}, status=404)
    

@csrf_exempt
def update_user(request):
    if not request.method == 'PATCH':
        return JsonResponse({'message': 'Http Method incorrected'})

    try:
        body = json.loads(request.body)
        user_id = body.get('id')

        response_user = get_object_or_404(Usuario, id_usuario=user_id)

        if not response_user:
            return JsonResponse({'message': 'User does not exist'}, status=404)

    except Http404:
            return JsonResponse({'message': 'User does not exist'}, status=404)

