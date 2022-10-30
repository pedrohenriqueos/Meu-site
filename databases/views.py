from urllib import response
from winreg import REG_WHOLE_HIVE_VOLATILE
from django.shortcuts import render
from .forms import NewData
from django.http import HttpResponseRedirect
from .models import SaveData, ResquestData, RequestAll

USERS = []

def databases(request): 
    return render(request,"Databases.html",{'header': "Banco de Dados",'USERS':USERS})

def formulario(request):
    form = NewData()
    return render(request,"form.html",{'header': "Formulário", 'form':form})

def create(request):
    form = NewData(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        address = form.cleaned_data["address"]
        city = form.cleaned_data["city"]
        state = form.cleaned_data["state"]
        cep = form.cleaned_data["cep"]
        check = form.cleaned_data["check"]
        output = SaveData( name, email, password, address, city, state, cep, check )
        USERS.append(output['id'])
        return render(request,"user.html",{'header':"Usuário "+name, 'dados':output})
    return render(request,"error.html")

def user(request, user):
    if user in USERS:
        dados = ResquestData(user)
        return render(request,"user.html",{'header':"Usuário "+dados['name'], 'dados':dados})
    return render(request,"NotFound.html",{'header':"Não Encontrado"})

def usuarios(request):
    dados = RequestAll(USERS)
    return render(request,"users.html",{'header':"Usuários", 'USERS':dados})