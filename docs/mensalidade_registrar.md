# Registrar Mensalidade

## O que faz
Registra um ou mais pagamentos de mensalidade para um intervalo de meses. O valor total informado é dividido igualmente entre os meses do intervalo. Os registros são criados com status `pendente` e aguardam aprovação do ADM.

**Exemplo:** Registrar R$ 150,00 de janeiro a março → cria 3 mensalidades de R$ 50,00 cada.

## Quem pode acessar
**Todos os usuários autenticados** (ADM e Filho).

- **Filho:** o registro é vinculado automaticamente ao próprio perfil; o campo `filho` não é exibido no formulário.
- **ADM:** pode escolher qualquer filho da lista para vincular o pagamento.

## Campos envolvidos
| Campo | Obrigatório | Descrição |
|---|---|---|
| `mes_inicio` | Sim | Mês inicial do intervalo (formato `YYYY-MM`) |
| `mes_fim` | Sim | Mês final do intervalo (formato `YYYY-MM`) |
| `valor` | Sim | Valor total a ser dividido pelos meses |
| `data_pagamento` | Não | Data em que o pagamento foi realizado |
| `comprovante` | Não | Arquivo de comprovante (imagem ou PDF) |
| `filho` | Só para ADM | ID do membro a ser vinculado |

## URLs

```
GET  /mensalidades/registrar/   → exibe o formulário
POST /mensalidades/registrar/   → processa o registro
```

## Exemplo de uso

O filho acessa `/mensalidades/registrar/`, informa:
- Mês início: `2025-05`
- Mês fim: `2025-06`
- Valor: `100.00`
- Comprovante: `comprovante_maio_junho.jpg`

Resultado: 2 mensalidades criadas (maio e junho) com valor R$ 50,00 cada, status `pendente`.
