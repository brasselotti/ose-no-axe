# Aprovar Mensalidade

## O que faz
Altera o status de uma mensalidade de `pendente` para `pago`, confirmando que o pagamento foi verificado e aceito pelo administrador.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
Não há formulário. A aprovação é feita com base no `pk` da mensalidade passado na URL. O campo `status` é alterado internamente para `pago`.

| Campo alterado | Valor anterior | Valor após aprovação |
|---|---|---|
| `status` | `pendente` | `pago` |

## URLs

### Interface HTML
```
GET /mensalidades/<pk>/aprovar/
```
> Redireciona para `/mensalidades/` após a ação.

### API REST
```
POST /api/mensalidades/<pk>/aprovar/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM visualiza a listagem de mensalidades pendentes e clica em "Aprovar" na mensalidade de ID 10. O status é atualizado para `pago` e o ADM é redirecionado para a listagem com mensagem de confirmação.

**API:**
```http
POST /api/mensalidades/10/aprovar/
Authorization: Bearer <token>
```
Resposta:
```json
{
  "mensagem": "Mensalidade de Maria de Oxum aprovada com sucesso."
}
```
