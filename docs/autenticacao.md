# Login e Logout

## O que faz
Gerencia o acesso ao sistema via sessão. O login autentica o usuário com username e senha; o logout encerra a sessão ativa e redireciona para a página de login.

## Quem pode acessar
**Público** (qualquer pessoa com credenciais cadastradas).

## Campos envolvidos

### Login
| Campo | Obrigatório | Descrição |
|---|---|---|
| `username` | Sim | Nome de usuário cadastrado |
| `password` | Sim | Senha do usuário |

### Logout
Sem campos. Apenas encerra a sessão atual.

## URLs

```
GET  /login/    → exibe o formulário de login
POST /login/    → autentica o usuário
GET  /logout/   → encerra a sessão e redireciona para /login/
GET  /          → redireciona automaticamente para /login/
GET  /home/     → página inicial após o login (requer autenticação)
```

## Exemplo de uso

**Login via formulário HTML:**
1. Usuário acessa `/login/`
2. Preenche `username` e `password`
3. Após autenticação bem-sucedida, é redirecionado para `/home/`
4. Em caso de erro, permanece na página com mensagem de falha

**Logout:**
Usuário acessa `/logout/` (geralmente via botão no menu) e é redirecionado para `/login/`.

## Observações
- Todas as rotas protegidas redirecionam para `/login/` caso o usuário não esteja autenticado (`@login_required`).
