from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from app.models import MeuObjeto
from app.serializers import MeuObjetoSerializer

import requests
# Create your views here.
def index(request, id=None):
    meu_obj = MeuObjeto(1, 'beto', 'sales')
    serializer = MeuObjetoSerializer(meu_obj)

    # meu_obj2 = requests.get('http://127.0.0.1:3000/meu_objeto/' + id)

    # serializer2 = MeuObjetoSerializer(data=meu_obj2.json())
    # serializer2.is_valid()

    return HttpResponse('olá abiguinho' + str(serializer.data))

def users(request):
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:3000/meu_objeto/')
        objs = [MeuObjetoSerializer(data=obj) for obj in response.json()]
        html = '<ul>'
        for obj in objs:
            if obj.is_valid():
                valid = obj.validated_data
                html += f"""
                    <li id='{valid['id']}'>
                        <a href='/usuario/{valid['id']}'>
                        {valid['nome']} {valid['sobrenome']}
                        </a>
                    </li>"""
        
        html += '</ul>'
        return HttpResponse(html)
    
    return HttpResponse("Page not found", status=404)

def user_detail(request, id=None):
    response = requests.get(f'http://127.0.0.1:3000/meu_objeto/{id}')
    obj = MeuObjetoSerializer(data=response.json())
    if obj.is_valid():
        valid = obj.validated_data
        return HttpResponse(f"{valid['id']} - {valid['nome']} {valid['sobrenome']}")
    else:
        return HttpResponse('Este usuário não foi localizado.')

def teste_ana(request):
    if request.method == 'GET':
        return HttpResponse('Sai daqui com o seu GET')
    if request.method == 'POST':
        return HttpResponse('pode ficar com seu POST lindo')
    return HttpResponse(str(request.method))