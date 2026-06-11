# Excluir Filho

## O que faz
Remove permanentemente um membro do sistema. Por causa do `on_delete=CASCADE` na model `Mensalidade`, todas as mensalidades vinculadas ao membro também são excluídas automaticamente.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A exclusão é realizada com base no `pk` (ID) do membro passado na URL.

## URLs

### Interface HTML
```
GET /filhos/<pk>/excluir/
```
> A exclusão ocorre diretamente ao acessar a URL (sem confirmação via formulário). Recomenda-se implementar um modal de confirmação no template.

### API REST
```
DELETE /api/filhos/<pk>/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM clica no botão "Excluir" ao lado do membro na listagem, o que dispara uma requisição para `/filhos/3/excluir/`. O membro e todas as suas mensalidades são removidos.

**API:**
```http
DELETE /api/filhos/3/
Authorization: Bearer <token>
```
Resposta: `204 No Content`

## Atenção
A exclusão é irreversível. Todas as mensalidades do membro são apagadas em cascata junto com o registro do filho.
