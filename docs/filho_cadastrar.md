# Cadastrar Filho

## O que faz
Cria um novo membro no sistema, gerando suas credenciais de acesso (username/senha) e registrando todas as informações pessoais e espirituais.

## Quem pode acessar
**Somente ADM.**

## Campos envolvidos

### Identificação e acesso
| Campo | Obrigatório | Descrição |
|---|---|---|
| `username` | Sim | Login de acesso ao sistema |
| `password` | Sim | Senha de acesso |
| `nome` | Sim | Nome completo |
| `telefone` | Não | Telefone de contato |
| `eh_administrador` | Não | Marcar se o membro será ADM |

### Endereço
| Campo | Obrigatório | Descrição |
|---|---|---|
| `endereco` | Não | Logradouro |
| `bairro` | Não | Bairro |
| `cidade` | Não | Cidade |
| `cep` | Não | CEP |

### Informações do médium
| Campo | Obrigatório | Descrição |
|---|---|---|
| `data_nascimento` | Não | Data de nascimento |
| `data_bori` | Não | Data do Bori |
| `filho_iniciado` | Não | Checkbox: se o membro foi iniciado |

### Dados da iniciação (liberados apenas se `filho_iniciado = True`)
| Campo | Obrigatório | Descrição |
|---|---|---|
| `data_iniciacao` | Não | Data da feitura |
| `ordem_posto` | Não | Ordem ou posto na hierarquia |
| `orixa` | Não | Orixá de cabeça |
| `orunko` | Não | Nome no santo (Orunkó) |
| `nome_ere` | Não | Nome do Erê |
| `madrinha_padrinho` | Não | Nome da madrinha ou padrinho |
| `mae_pai_pequeno` | Não | Nome da mãe/pai pequeno |

## URLs

### Interface HTML
```
GET  /filhos/cadastrar/   → exibe o formulário
POST /filhos/cadastrar/   → processa o cadastro
```

### API REST
```
POST /api/filhos/
```
> Requer autenticação JWT com perfil ADM.

## Exemplo de uso

**HTML:** ADM acessa `/filhos/cadastrar/`, preenche o formulário e submete. Após o cadastro bem-sucedido, é redirecionado para `/filhos/`.

**API:**
```http
POST /api/filhos/
Authorization: Bearer <token>
Content-Type: application/json

{
  "username": "maria_oxum",
  "password": "senha123",
  "nome": "Maria de Oxum",
  "telefone": "84988880000",
  "filho_iniciado": true,
  "orixa": "Oxum",
  "orunko": "Omilayó"
}
```
