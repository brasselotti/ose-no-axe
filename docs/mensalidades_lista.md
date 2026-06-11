# Listar Mensalidades

## O que faz
Exibe as mensalidades separadas em três grupos: **Pendentes**, **Pagas** e **Recusadas**. O ADM visualiza as mensalidades de todos os membros e pode filtrar por nome. O filho comum visualiza apenas as suas próprias.

## Quem pode acessar
- **ADM:** vê todas as mensalidades do sistema, com filtro por nome do filho.
- **Filho:** vê apenas as próprias mensalidades.

## Campos exibidos
| Campo | Descrição |
|---|---|
| `filho` | Nome do membro vinculado |
| `mes_referencia` | Mês/ano da competência (armazenado como dia 1 do mês) |
| `valor` | Valor pago |
| `status` | `pendente`, `pago`, `atrasado` ou `recusado` |
| `comprovante` | Arquivo de comprovante de pagamento (se enviado) |
| `data_pagamento` | Data informada pelo membro no momento do registro |

## URLs

### Interface HTML
```
GET /mensalidades/
GET /mensalidades/?filho=<nome>   → filtro por nome (ADM apenas)
```

### API REST
```
GET /api/mensalidades/
```
> ADM recebe todas. Filho recebe apenas as próprias. Ordenadas por `-mes_referencia`.

## Exemplo de uso

**HTML (ADM filtrando por nome):**
```
/mensalidades/?filho=Maria
```
Retorna as mensalidades de todos os membros cujo nome contém "Maria".

**API:**
```http
GET /api/mensalidades/
Authorization: Bearer <token>
```
Resposta (filho comum):
```json
[
  {
    "id": 10,
    "filho": 5,
    "mes_referencia": "2025-06-01",
    "valor": "50.00",
    "status": "pendente",
    "data_pagamento": "2025-06-05"
  }
]
```
