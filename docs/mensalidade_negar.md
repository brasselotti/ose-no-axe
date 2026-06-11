# Negar Mensalidade

## O que faz
Recusa uma solicitação de pagamento de mensalidade. O status é alterado para `recusado` tanto na interface HTML quanto na API REST.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A negação é feita com base no `pk` da mensalidade passado na URL.

| Campo alterado | Valor anterior | Valor após negação |
|---|---|---|
| `status` | `pendente` | `recusado` |

## URLs

### Interface HTML
```
GET /mensalidades/<pk>/negar/
```
> Redireciona para `/mensalidades/` após a ação.

### API REST
```
POST /api/mensalidades/<pk>/negar/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM visualiza um comprovante inválido na listagem e clica em "Negar". A mensalidade de ID 7 tem seu status alterado para `recusado`.

**API:**
```http
POST /api/mensalidades/7/negar/
Authorization: Bearer <token>
```
Resposta:
```json
{
  "mensagem": "Solicitação de João de Ogum negada."
}
```
