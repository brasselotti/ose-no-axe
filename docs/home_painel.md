# Painel Inicial (Home)

## O que faz
Exibe a página inicial do sistema após o login. Para ADMs, apresenta um painel de gestão com a lista de inadimplentes e membros isentos do mês corrente. Para filhos comuns, exibe apenas a tela de boas-vindas.

## Quem pode acessar
**Todos os usuários autenticados.** O conteúdo exibido varia conforme o perfil.

## Conteúdo exibido

### Para ADM
| Seção | Descrição |
|---|---|
| Inadimplentes | Filhos que **não** registraram pagamento no mês atual e **não** estão isentos, ordenados por nome |
| Total de inadimplentes | Contagem dos inadimplentes |
| Isentos do mês | Filhos com isenção registrada para o mês atual, com motivo e quem criou |
| Total de isentos | Contagem dos isentos |
| Mês atual | Data de referência usada nos cálculos (dia 1 do mês corrente) |

### Para Filho
Página de boas-vindas sem dados adicionais.

## URLs

```
GET /home/
```
> Redireciona para `/login/` caso o usuário não esteja autenticado.

## Lógica de inadimplência

Um filho é considerado inadimplente no mês atual quando:
1. **Não** possui nenhuma `Mensalidade` com `mes_referencia` igual ao dia 1 do mês corrente, **e**
2. **Não** possui um registro em `IsentoMes` para o mesmo mês.

## Exemplo de uso

ADM acessa `/home/` e visualiza que 3 membros ainda não registraram pagamento para o mês atual. Um deles está isento com o motivo "Viagem de trabalho". Os outros dois aparecem na lista de inadimplentes com um botão para isentá-los diretamente do painel.
