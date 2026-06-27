# Excluir Mensalidade

## O que faz
Remove permanentemente um registro de mensalidade do sistema. A operação não pode ser desfeita.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A exclusão é realizada com base no `pk` da mensalidade passado na URL.

## URLs

```
GET /mensalidades/<pk>/excluir/
```
> Redireciona para `/mensalidades/` após a ação.

## Exemplo de uso

ADM acessa `/mensalidades/12/excluir/` para remover um lançamento duplicado.
