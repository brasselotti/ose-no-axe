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

```
GET  /financeiro/registrar/   → exibe o formulário
POST /financeiro/registrar/   → salva a movimentação
```

## Exemplo de uso

ADM acessa `/financeiro/registrar/` e registra uma doação:
- Descrição: `Doação de ogã`
- Valor: `200.00`
- Tipo: `entrada`
- Data: `2025-06-10`
