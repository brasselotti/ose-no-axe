# Negar Mensalidade

## O que faz
Recusa uma solicitação de pagamento de mensalidade. O status é alterado para `recusado`.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A negação é feita com base no `pk` da mensalidade passado na URL.

| Campo alterado | Valor anterior | Valor após negação |
|---|---|---|
| `status` | `pendente` | `recusado` |

## URLs

```
GET /mensalidades/<pk>/negar/
```
> Redireciona para `/mensalidades/` após a ação.

## Exemplo de uso

ADM visualiza um comprovante inválido na listagem e clica em "Negar". A mensalidade de ID 7 tem seu status alterado para `recusado`.
