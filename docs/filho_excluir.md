# Excluir Filho

## O que faz
Remove permanentemente um membro do sistema. Por causa do `on_delete=CASCADE` na model `Mensalidade`, todas as mensalidades vinculadas ao membro também são excluídas automaticamente.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A exclusão é realizada com base no `pk` (ID) do membro passado na URL.

## URLs

```
GET /filhos/<pk>/excluir/
```

## Exemplo de uso

ADM clica no botão "Excluir" ao lado do membro na listagem, o que dispara uma requisição para `/filhos/3/excluir/`. O membro e todas as suas mensalidades são removidos.

## Atenção
A exclusão é irreversível. Todas as mensalidades do membro são apagadas em cascata junto com o registro do filho.
