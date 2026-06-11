# Autenticação via API (JWT)

## O que faz
Fornece tokens JWT (JSON Web Token) para autenticação nas rotas da API REST. O token de acesso tem validade curta; o token de refresh é usado para obter um novo token de acesso sem re-autenticar.

## Quem pode acessar
**Público** (qualquer pessoa com credenciais cadastradas).

## Campos envolvidos

### Obter token
| Campo | Obrigatório | Descrição |
|---|---|---|
| `username` | Sim | Nome de usuário |
| `password` | Sim | Senha do usuário |

### Renovar token
| Campo | Obrigatório | Descrição |
|---|---|---|
| `refresh` | Sim | Token de refresh obtido anteriormente |

## URLs

```
POST /api/token/          → obtém access token e refresh token
POST /api/token/refresh/  → renova o access token
```

## Exemplo de uso

**Obter token:**
```http
POST /api/token/
Content-Type: application/json

{
  "username": "fabiano",
  "password": "minha_senha"
}
```
Resposta:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Usar o token nas chamadas à API:**
```http
GET /api/filhos/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Renovar token expirado:**
```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
Resposta:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Observações
- O token JWT é usado **exclusivamente nas rotas `/api/`**.
- Para as rotas HTML (`/filhos/`, `/mensalidades/`, etc.), a autenticação é feita via sessão (login no formulário `/login/`).
