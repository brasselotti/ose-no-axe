from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensalidade, IsentoMes


# ---- Views HTML ----

@login_required(login_url='/login/')
def mensalidades_lista(request):
    filtro_filho = request.GET.get('filho', '')

    if request.user.eh_administrador:
        qs = Mensalidade.objects.all()
        if filtro_filho:
            qs = qs.filter(filho__nome__icontains=filtro_filho)
    else:
        qs = Mensalidade.objects.filter(filho=request.user)

    pendentes = qs.filter(status='pendente').order_by('-mes_referencia')
    pagas = qs.filter(status='pago').order_by('-mes_referencia')
    recusadas = qs.filter(status='recusado').order_by('-mes_referencia')

    return render(request, 'mensalidades/lista.html', {
        'pendentes': pendentes,
        'pagas': pagas,
        'recusadas': recusadas,
        'filtro_filho': filtro_filho,
    })


@login_required(login_url='/login/')
def mensalidade_registrar(request):
    if request.method == 'POST':
        filho = request.user if not request.user.eh_administrador else None
        mes_inicio = request.POST.get('mes_inicio')
        mes_fim = request.POST.get('mes_fim')
        valor = request.POST.get('valor')
        data_pagamento = request.POST.get('data_pagamento')
        comprovante = request.FILES.get('comprovante')

        if not filho and request.user.eh_administrador:
            from filhos.models import Filho
            filho_id = request.POST.get('filho')
            filho = get_object_or_404(Filho, pk=filho_id)

        # Calcula quantos meses estão no intervalo
        from datetime import date
        ano_inicio, mes_inicio_num = map(int, mes_inicio.split('-'))
        ano_fim, mes_fim_num = map(int, mes_fim.split('-'))

        total_meses = (ano_fim - ano_inicio) * 12 + (mes_fim_num - mes_inicio_num) + 1
        valor_por_mes = round(float(valor) / total_meses, 2)

        ano, mes = ano_inicio, mes_inicio_num
        while (ano, mes) <= (ano_fim, mes_fim_num):
            Mensalidade.objects.create(
                filho=filho,
                mes_referencia=date(ano, mes, 1),
                valor=valor_por_mes,
                comprovante=comprovante,
                status='pendente',
                data_pagamento=data_pagamento or None,
            )
            mes += 1
            if mes > 12:
                mes = 1
                ano += 1

        messages.success(request, 'Pagamento(s) registrado(s)! Aguarde a aprovação do ADM.')
        return redirect('/mensalidades/')

    if request.user.eh_administrador:
        from filhos.models import Filho
        filhos = Filho.objects.all().order_by('nome')
    else:
        filhos = None

    return render(request, 'mensalidades/form.html', {'filhos': filhos})


@login_required(login_url='/login/')
def mensalidade_aprovar(request, pk):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/mensalidades/')
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    mensalidade.status = 'pago'
    mensalidade.save()
    messages.success(request, f'Mensalidade de {mensalidade.filho.nome} aprovada!')
    return redirect('/mensalidades/')


@login_required(login_url='/login/')
def mensalidade_negar(request, pk):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/mensalidades/')
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    mensalidade.status = 'recusado'
    mensalidade.save()
    messages.warning(request, f'Solicitação de {mensalidade.filho.nome} recusada.')
    return redirect('/mensalidades/')


@login_required(login_url='/login/')
def mensalidade_excluir(request, pk):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/mensalidades/')
    mensalidade = get_object_or_404(Mensalidade, pk=pk)
    mensalidade.delete()
    messages.success(request, 'Mensalidade removida com sucesso.')
    return redirect('/mensalidades/')

@login_required(login_url='/login/')
def isentar_filho(request, filho_id):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/home/')

    from django.utils import timezone
    from filhos.models import Filho

    hoje = timezone.now().date()
    mes_atual = hoje.replace(day=1)
    filho = get_object_or_404(Filho, pk=filho_id)
    motivo = request.POST.get('motivo', '')

    IsentoMes.objects.get_or_create(
        filho=filho,
        mes_referencia=mes_atual,
        defaults={
            'motivo': motivo,
            'criado_por': request.user,
        }
    )

    messages.success(request, f'{filho.nome} desconsiderado para o mês atual.')
    return redirect('/home/')