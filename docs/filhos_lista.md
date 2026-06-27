# Listar Filhos

## O que faz
Exibe a lista completa de todos os membros (filhos de santo) cadastrados no sistema, ordenados por nome.

## Quem pode acessar
**Somente ADM.** Filhos comuns são redirecionados para `/home/` com mensagem de erro.

## Campos exibidos
| Campo | Descrição |
|---|---|
| `nome` | Nome completo do membro |
| `username` | Login do membro |
| `telefone` | Telefone de contato |
| `cidade` | Cidade de residência |
| `filho_iniciado` | Se o membro já foi iniciado no culto |
| `eh_administrador` | Se o membro tem perfil de ADM |

## URLs

```
GET /filhos/
```

## Exemplo de uso

ADM acessa `/filhos/` e visualiza a tabela com todos os membros.
