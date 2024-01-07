from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .forms import *
from .models import Key_Panel
from datetime import datetime

def index(request):
    #Retorna o ultimo check in feito(horario mais próximo de agora)
    try:
        status= Key_Panel.objects.filter(check_in__lte=datetime.time(datetime.now()),check_out=None).order_by('-check_in')[0]
    except:
        status=False

    return render(request,'gym/index.html',{'status':status})

def signIn(request):
    if request.user.username.endswith('Viver'):#Checa se usuário já esta logado
        return redirect('admin_panel')
    signIn=Sign_In()
    if request.method == 'POST':
        form=Sign_In(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('admin_panel')
                else:
                    messages.error(request, 'Usuário Inativo')
                    return redirect('login')
            else:
                messages.error(request,'Usuário ou senha incorreta')
                return redirect('login')
    return render(request,'gym/login.html',{'login':signIn})

@login_required(login_url='login')
def admin_panel(request):
    #Retorna os 5 ultimos registros realizados
    last_five=Key_Panel.objects.filter(check_in__lte=datetime.time(datetime.now())).order_by('-check_in')[0:5]
    gym_open=''
    for last in last_five:
        if last.check_out ==None:
            gym_open=last.id#O registro mais antigo se torna o primeiro a ser encerrado pela API_UPDATE
    if request.method =='POST':
        name=request.POST.get('name',None)
        new=Key_Panel(resident=name)
        new.save()
        messages.success(request,f'Registro {name} adicionado')
        return redirect('admin_panel')
    return render(request,'gym/admin_panel.html',{'last_five':last_five,'open':gym_open})

def api_update(request,id):
    Key_Panel.objects.filter(id=id).update(check_out=datetime.time(datetime.now()))
    messages.success(request,'Registro Atualizado')
    return redirect('admin_panel')