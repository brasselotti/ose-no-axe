from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Movimentacao


# ---- Views HTML ----

@login_required(login_url='/login/')
def financeiro_lista(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data')
    entradas = Movimentacao.objects.filter(tipo='entrada').aggregate(total=Sum('valor'))['total'] or 0
    saidas = Movimentacao.objects.filter(tipo='saida').aggregate(total=Sum('valor'))['total'] or 0
    saldo = entradas - saidas

    return render(request, 'financeiro/lista.html', {
        'movimentacoes': movimentacoes,
        'entradas': entradas,
        'saidas': saidas,
        'saldo': saldo,
    })


@login_required(login_url='/login/')
def movimentacao_registrar(request):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/financeiro/')

    if request.method == 'POST':
        Movimentacao.objects.create(
            descricao=request.POST.get('descricao'),
            valor=request.POST.get('valor'),
            tipo=request.POST.get('tipo'),
            data=request.POST.get('data'),
            observacao=request.POST.get('observacao', ''),
        )
        messages.success(request, 'Movimentação registrada com sucesso!')
        return redirect('/financeiro/')

    return render(request, 'financeiro/form.html')


@login_required(login_url='/login/')
def movimentacao_excluir(request, pk):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/financeiro/')
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    movimentacao.delete()
    messages.success(request, 'Movimentação removida com sucesso.')
    return redirect('/financeiro/')