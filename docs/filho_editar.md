# Editar Filho

## O que faz
Atualiza os dados de um membro existente. O ADM pode editar qualquer membro e alterar o perfil de administrador. O próprio filho pode editar apenas o seu cadastro (sem alterar o campo `eh_administrador`).

## Quem pode acessar
- **ADM:** pode editar qualquer membro e modificar o campo `eh_administrador`.
- **Filho:** pode editar apenas o próprio cadastro. Tentativa de editar outro membro resulta em redirecionamento para `/home/`.

## Campos envolvidos
Os mesmos do cadastro, com exceção de `username` (não alterável por esta view). A senha só é alterada se o campo `password` for preenchido no formulário.

| Campo | ADM pode editar | Filho pode editar |
|---|---|---|
| `nome` | Sim | Sim |
| `telefone` | Sim | Sim |
| `endereco`, `bairro`, `cidade`, `cep` | Sim | Sim |
| `data_nascimento`, `data_bori` | Sim | Sim |
| `filho_iniciado` | Sim | Sim |
| `data_iniciacao`, `ordem_posto`, `orixa`, `orunko`, `nome_ere`, `madrinha_padrinho`, `mae_pai_pequeno` | Sim | Sim |
| `password` | Sim | Sim |
| `eh_administrador` | Sim | **Não** |

## URLs

```
GET  /filhos/<pk>/editar/   → exibe formulário preenchido
POST /filhos/<pk>/editar/   → salva as alterações
```

## Exemplo de uso

Filho acessa `/filhos/5/editar/`, atualiza seu telefone e salva.
