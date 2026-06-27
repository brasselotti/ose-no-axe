# Listar Movimentações e Saldo

## O que faz
Exibe todas as movimentações financeiras do terreiro (entradas e saídas) em ordem decrescente de data, além de um resumo com o total de entradas, total de saídas e o saldo atual.

## Quem pode acessar
**Todos os usuários autenticados** (ADM e Filho). A transparência financeira é um objetivo central do sistema.

## Campos exibidos
| Campo | Descrição |
|---|---|
| `descricao` | Descrição da movimentação |
| `valor` | Valor em reais |
| `tipo` | `entrada` (Doação/Arrecadação) ou `saida` (Custo/Despesa) |
| `data` | Data da movimentação |
| `observacao` | Texto livre com detalhes adicionais |

### Resumo financeiro exibido no topo
| Item | Descrição |
|---|---|
| Total de Entradas | Soma de todas as movimentações do tipo `entrada` |
| Total de Saídas | Soma de todas as movimentações do tipo `saida` |
| Saldo Atual | Entradas − Saídas |

## URLs

```
GET /financeiro/
```

## Exemplo de uso

Qualquer membro logado acessa `/financeiro/` e visualiza o histórico de movimentações e o saldo atual do terreiro.
