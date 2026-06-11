# Registrar Movimentação Financeira

## O que faz
Cria um novo lançamento financeiro no sistema, podendo ser uma entrada (doação, arrecadação) ou uma saída (custo, despesa).

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
| Campo | Obrigatório | Descrição |
|---|---|---|
| `descricao` | Sim | Descrição resumida da movimentação |
| `valor` | Sim | Valor em reais (decimal, ex: `150.00`) |
| `tipo` | Sim | `entrada` ou `saida` |
| `data` | Sim | Data da movimentação (formato `YYYY-MM-DD`) |
| `observacao` | Não | Detalhes adicionais em texto livre |

## URLs

### Interface HTML
```
GET  /financeiro/registrar/   → exibe o formulário
POST /financeiro/registrar/   → salva a movimentação
```

### API REST
```
POST /api/movimentacoes/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM acessa `/financeiro/registrar/` e registra uma doação:
- Descrição: `Doação de ogã`
- Valor: `200.00`
- Tipo: `entrada`
- Data: `2025-06-10`

**API:**
```http
POST /api/movimentacoes/
Authorization: Bearer <token>
Content-Type: application/json

{
  "descricao": "Compra de velas para ritual",
  "valor": "85.50",
  "tipo": "saida",
  "data": "2025-06-08",
  "observacao": "Comprado no mercado central"
}
```
Resposta: `201 Created`
```json
{
  "id": 15,
  "descricao": "Compra de velas para ritual",
  "valor": "85.50",
  "tipo": "saida",
  "data": "2025-06-08",
  "observacao": "Comprado no mercado central"
}
```
