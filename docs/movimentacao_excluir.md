# Excluir Movimentação Financeira

## O que faz
Remove permanentemente um lançamento financeiro do sistema. A operação afeta o saldo calculado, pois entradas e saídas são recalculadas dinamicamente a cada consulta.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A exclusão é realizada com base no `pk` da movimentação passado na URL.

## URLs

### Interface HTML
```
GET /financeiro/<pk>/excluir/
```
> Redireciona para `/financeiro/` após a ação.

### API REST
```
DELETE /api/movimentacoes/<pk>/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM identifica um lançamento duplicado na listagem e acessa `/financeiro/8/excluir/` para removê-lo.

**API:**
```http
DELETE /api/movimentacoes/8/
Authorization: Bearer <token>
```
Resposta: `204 No Content`

## Atenção
A exclusão é irreversível. Como o saldo é calculado dinamicamente, remover uma entrada reduz o saldo e remover uma saída o aumenta.
