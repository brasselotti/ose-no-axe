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

```
GET /mensalidades/
GET /mensalidades/?filho=<nome>   → filtro por nome (ADM apenas)
```

## Exemplo de uso

ADM filtrando por nome:
```
/mensalidades/?filho=Maria
```
Retorna as mensalidades de todos os membros cujo nome contém "Maria".
