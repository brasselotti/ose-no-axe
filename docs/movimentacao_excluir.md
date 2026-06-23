# Excluir Movimentação Financeira

## O que faz
Remove permanentemente um lançamento financeiro do sistema. A operação afeta o saldo calculado, pois entradas e saídas são recalculadas dinamicamente a cada consulta.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A exclusão é realizada com base no `pk` da movimentação passado na URL.

## URLs

```
GET /financeiro/<pk>/excluir/
```
> Redireciona para `/financeiro/` após a ação.

## Exemplo de uso

ADM identifica um lançamento duplicado na listagem e acessa `/financeiro/8/excluir/` para removê-lo.

## Atenção
A exclusão é irreversível. Como o saldo é calculado dinamicamente, remover uma entrada reduz o saldo e remover uma saída o aumenta.
