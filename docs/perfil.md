# Editar Perfil

## O que faz
Permite que qualquer usuário autenticado edite o próprio perfil: dados pessoais, endereço, login e senha. Diferente de `/filhos/<pk>/editar/`, esta view também permite alterar o `username` e é acessível diretamente pelo próprio membro sem intervenção do ADM.

## Quem pode acessar
**Todos os usuários autenticados** (ADM e Filho), exclusivamente para o próprio perfil.

## Campos envolvidos
| Campo | Obrigatório | Descrição |
|---|---|---|
| `username` | Não | Novo login de acesso (validado para garantir unicidade) |
| `nome` | Não | Nome completo |
| `telefone` | Não | Telefone de contato |
| `endereco` | Não | Logradouro |
| `bairro` | Não | Bairro |
| `cidade` | Não | Cidade |
| `cep` | Não | CEP |
| `password` | Não | Nova senha (só alterada se o campo for preenchido) |

> Campos não enviados mantêm o valor atual.

## URLs

```
GET  /perfil/   → exibe o formulário preenchido com os dados atuais
POST /perfil/   → salva as alterações
```

## Validações
- Se o novo `username` já estiver em uso por outro membro, a alteração é recusada com mensagem de erro e o formulário é reexibido.
- A senha só é atualizada se o campo `password` for enviado com valor não vazio.

## Exemplo de uso

Membro acessa `/perfil/`, altera seu telefone e define uma nova senha. Ao salvar, é redirecionado para `/perfil/` com mensagem de confirmação.
