# Documentação — Osé no Axé

Sistema de gestão administrativa do Terreiro da Prata (Ilê Axé Afinká).

---

## Módulos

### Filhos (Membros)
| Funcionalidade | Acesso | Arquivo |
|---|---|---|
| Listar filhos | ADM | [filhos_lista.md](filhos_lista.md) |
| Cadastrar filho | ADM | [filho_cadastrar.md](filho_cadastrar.md) |
| Editar filho | ADM ou próprio filho | [filho_editar.md](filho_editar.md) |
| Excluir filho | ADM | [filho_excluir.md](filho_excluir.md) |

### Mensalidades
| Funcionalidade | Acesso | Arquivo |
|---|---|---|
| Listar mensalidades | ADM (todas) / Filho (próprias) | [mensalidades_lista.md](mensalidades_lista.md) |
| Registrar mensalidade | Todos os usuários logados | [mensalidade_registrar.md](mensalidade_registrar.md) |
| Aprovar mensalidade | ADM | [mensalidade_aprovar.md](mensalidade_aprovar.md) |
| Negar mensalidade | ADM | [mensalidade_negar.md](mensalidade_negar.md) |
| Excluir mensalidade | ADM | [mensalidade_excluir.md](mensalidade_excluir.md) |
| Isentar filho do mês | ADM | [mensalidade_isentar.md](mensalidade_isentar.md) |

### Financeiro
| Funcionalidade | Acesso | Arquivo |
|---|---|---|
| Listar movimentações e saldo | Todos os usuários logados | [financeiro_lista.md](financeiro_lista.md) |
| Registrar movimentação | ADM | [movimentacao_registrar.md](movimentacao_registrar.md) |
| Excluir movimentação | ADM | [movimentacao_excluir.md](movimentacao_excluir.md) |

### Painel / Perfil
| Funcionalidade | Acesso | Arquivo |
|---|---|---|
| Painel inicial (inadimplentes e isentos) | Todos os usuários logados | [home_painel.md](home_painel.md) |
| Editar próprio perfil | Todos os usuários logados | [perfil.md](perfil.md) |

### Autenticação
| Funcionalidade | Acesso | Arquivo |
|---|---|---|
| Login / Logout (HTML) | Público | [autenticacao.md](autenticacao.md) |

---

## Perfis de Usuário

| Perfil | Descrição |
|---|---|
| **ADM** | Usuário com `eh_administrador = True`. Acesso total ao sistema. |
| **Filho** | Usuário comum. Acesso restrito ao próprio perfil e às próprias mensalidades. |
