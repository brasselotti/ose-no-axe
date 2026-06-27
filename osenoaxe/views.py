from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from filhos.models import Filho
from mensalidades.models import Mensalidade, IsentoMes


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home/')
        else:
            error = 'Usuário ou senha incorretos.'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    contexto = {}

    if request.user.eh_administrador:
        hoje = timezone.now().date()
        mes_atual = hoje.replace(day=1)

        # Filhos que já registraram pagamento no mês atual
        filhos_pagaram = Mensalidade.objects.filter(
            mes_referencia=mes_atual
        ).values_list('filho_id', flat=True)

        # Filhos isentos no mês atual
        filhos_isentos_ids = IsentoMes.objects.filter(
            mes_referencia=mes_atual
        ).values_list('filho_id', flat=True)

        # Inadimplentes = todos os filhos - quem pagou - quem está isento
        inadimplentes = list(
            Filho.objects.exclude(
                id__in=filhos_pagaram
            ).exclude(
                id__in=filhos_isentos_ids
            ).order_by('nome')
        )

        # Isentos do mês com motivo
        isentos = IsentoMes.objects.filter(
            mes_referencia=mes_atual
        ).select_related('filho', 'criado_por')

        contexto['inadimplentes'] = inadimplentes
        contexto['total_inadimplentes'] = len(inadimplentes)
        contexto['isentos'] = isentos
        contexto['total_isentos'] = isentos.count()
        contexto['mes_atual'] = mes_atual

    return render(request, 'home.html', contexto)


@login_required(login_url='/login/')
def perfil_view(request):
    if request.method == 'POST':
        user = request.user
        novo_username = request.POST.get('username', '').strip()

        # Valida se o novo username já existe para outro usuário
        if novo_username and novo_username != user.username:
            from filhos.models import Filho
            if Filho.objects.filter(username=novo_username).exclude(pk=user.pk).exists():
                messages.error(request, 'Este login já está em uso por outro usuário.')
                return redirect('/perfil/')
            user.username = novo_username

        user.nome = request.POST.get('nome', user.nome)
        user.telefone = request.POST.get('telefone', user.telefone)
        user.endereco = request.POST.get('endereco', user.endereco)
        user.bairro = request.POST.get('bairro', user.bairro)
        user.cidade = request.POST.get('cidade', user.cidade)
        user.cep = request.POST.get('cep', user.cep)
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))
        user.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('/perfil/')
    return render(request, 'perfil.html')