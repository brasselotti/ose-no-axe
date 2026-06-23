from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Filho


# ---- Views HTML ----

@login_required(login_url='/login/')
def filhos_lista(request):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/home/')
    filhos = Filho.objects.all().order_by('nome')
    return render(request, 'filhos/lista.html', {'filhos': filhos})


@login_required(login_url='/login/')
def filho_cadastrar(request):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/home/')

    if request.method == 'POST':
        dados = request.POST
        try:
            filho = Filho.objects.create_user(
                username=dados['username'],
                password=dados['password'],
                nome=dados.get('nome', ''),
                telefone=dados.get('telefone', ''),
                endereco=dados.get('endereco', ''),
                bairro=dados.get('bairro', ''),
                cidade=dados.get('cidade', ''),
                cep=dados.get('cep', ''),
                data_nascimento=dados.get('data_nascimento') or None,
                data_bori=dados.get('data_bori') or None,
                filho_iniciado='filho_iniciado' in dados,
                data_iniciacao=dados.get('data_iniciacao') or None,
                ordem_posto=dados.get('ordem_posto', ''),
                orixa=dados.get('orixa', ''),
                orunko=dados.get('orunko', ''),
                nome_ere=dados.get('nome_ere', ''),
                madrinha_padrinho=dados.get('madrinha_padrinho', ''),
                mae_pai_pequeno=dados.get('mae_pai_pequeno', ''),
                eh_administrador='eh_administrador' in dados,
            )
            messages.success(request, f'Filho {filho.nome} cadastrado com sucesso!')
            return redirect('/filhos/')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {e}')

    return render(request, 'filhos/form.html', {'acao': 'Cadastrar'})


@login_required(login_url='/login/')
def filho_editar(request, pk):
    if not request.user.eh_administrador and request.user.pk != pk:
        messages.error(request, 'Você não tem permissão para editar este cadastro.')
        return redirect('/home/')

    filho = get_object_or_404(Filho, pk=pk)

    if request.method == 'POST':
        dados = request.POST
        filho.nome = dados.get('nome', filho.nome)
        filho.telefone = dados.get('telefone', filho.telefone)
        filho.endereco = dados.get('endereco', filho.endereco)
        filho.bairro = dados.get('bairro', filho.bairro)
        filho.cidade = dados.get('cidade', filho.cidade)
        filho.cep = dados.get('cep', filho.cep)
        filho.data_nascimento = dados.get('data_nascimento') or filho.data_nascimento
        filho.data_bori = dados.get('data_bori') or filho.data_bori
        filho.filho_iniciado = 'filho_iniciado' in dados
        filho.data_iniciacao = dados.get('data_iniciacao') or None
        filho.ordem_posto = dados.get('ordem_posto', filho.ordem_posto)
        filho.orixa = dados.get('orixa', filho.orixa)
        filho.orunko = dados.get('orunko', filho.orunko)
        filho.nome_ere = dados.get('nome_ere', filho.nome_ere)
        filho.madrinha_padrinho = dados.get('madrinha_padrinho', filho.madrinha_padrinho)
        filho.mae_pai_pequeno = dados.get('mae_pai_pequeno', filho.mae_pai_pequeno)
        if request.user.eh_administrador:
            filho.eh_administrador = 'eh_administrador' in dados
        if dados.get('password'):
            filho.set_password(dados['password'])
        filho.save()
        messages.success(request, 'Cadastro atualizado com sucesso!')
        return redirect('/filhos/')

    return render(request, 'filhos/form.html', {'acao': 'Editar', 'filho': filho})


@login_required(login_url='/login/')
def filho_excluir(request, pk):
    if not request.user.eh_administrador:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('/home/')
    filho = get_object_or_404(Filho, pk=pk)
    filho.delete()
    messages.success(request, 'Filho removido com sucesso.')
    return redirect('/filhos/')