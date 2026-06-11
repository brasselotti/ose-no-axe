# Excluir Mensalidade

## O que faz
Remove permanentemente um registro de mensalidade do sistema. A operação não pode ser desfeita.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A exclusão é realizada com base no `pk` da mensalidade passado na URL.

## URLs

### Interface HTML
```
GET /mensalidades/<pk>/excluir/
```
> Redireciona para `/mensalidades/` após a ação.

### API REST
```
DELETE /api/mensalidades/<pk>/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM acessa `/mensalidades/12/excluir/` para remover um lançamento duplicado.

**API:**
```http
DELETE /api/mensalidades/12/
Authorization: Bearer <token>
```
Resposta: `204 No Content`
