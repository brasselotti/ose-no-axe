# Isentar Filho do Mês

## O que faz
Registra uma isenção de mensalidade para um membro no mês corrente. O membro isento deixa de aparecer na lista de inadimplentes do painel do ADM. A isenção é idempotente: chamar a rota duas vezes para o mesmo membro/mês não cria duplicatas.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos
| Campo | Obrigatório | Descrição |
|---|---|---|
| `motivo` | Não | Texto livre justificando a isenção |

O mês de referência é calculado automaticamente como o dia 1 do mês atual no servidor. O membro é identificado pelo `filho_id` passado na URL.

## URLs

```
POST /mensalidades/isentar/<filho_id>/
```
> Redireciona para `/home/` após a ação.

## Model relacionada
`IsentoMes` — armazena `filho`, `mes_referencia`, `motivo` e `criado_por` (ADM que criou a isenção).

## Exemplo de uso

ADM está no painel `/home/` e clica em "Isentar" ao lado de um membro inadimplente. O formulário envia `motivo` (opcional) para `/mensalidades/isentar/7/`. O membro some da lista de inadimplentes e aparece na seção de isentos com o motivo informado.
