# Osé no Axé

<p align="center">
  <img src="static/images/logo.png" alt="Logo Ilê Axé Afinká" width="160">
</p>

## Identificação

> Fabiano Brasselotti dos Santos
>
> 20230030400
>
> ECT3699 - Desenvolvimento Web Front End - T01
>
> Título: Osé no Axé
>
> Slogan: Para dar um axé na administração do seu terreiro

## Descrição geral

Uma aplicação web desenvolvida em Django para membros de terreiros de candomblé, que realiza cadastros e gerencia registros de pagamentos de mensalidades por meio de páginas objetivas e claras.

O Terreiro da Prata (Ilê Axé Afinká), tomado como referência para desenvolvimento deste projeto, está situado no município de Macaíba-RN, no qual o autor deste trabalho é um membro ativo.

Considerando a vivência no espaço, pôde-se notar problemas como: a falta de conhecimento integral sobre os filhos da casa e ineficiência tecnológica para o controle de pagamento de mensalidades, que gera retrabalhos contínuos.

O sistema oferece interfaces para gerir o cadastro de pessoas no banco de dados e os pagamentos de mensalidades, buscando maior conhecimento sobre os membros e eliminando problemas causados pelo retrabalho manual com planilhas.

Não pretendemos tornar o "Osé no Axé" em uma rede social, onde os membros interajam entre si, nem uma plataforma para realizar os pagamentos, como um banco digital.

## Público-alvo & Personas

O "Osé no Axé" foi pensado para a utilização na comunidade de membros de terreiros de candomblé. Há dois tipos de perfil: **ADM**, com acesso integral às funcionalidades; e **Filho**, com acesso restrito ao próprio cadastro e ao registro de pagamento mensal via envio de comprovante.

Essas demandas se fazem importantes para que haja fidelidade quanto aos dados dos membros e para otimizar o controle de mensalidades, que atualmente é feito através de grupos do WhatsApp, repassando listas repetidamente a cada pagamento realizado.

## Listagem de funcionalidades

**MUST-01 // Cadastro**
Como filho da casa, quero me registrar no banco de dados da casa para salvar os meus dados.
- Validação de login (sem repetição entre membros);
- Data de bori obrigatória (somente se torna filho após o bori);
- Redireciona para `/home/` após sucesso;

**MUST-02 // Edição de cadastro**
Como filho da casa, quero atualizar os dados do meu cadastro para mantê-los atualizados.
- Precisa estar logado;
- ADM pode editar qualquer membro;

**MUST-03 // Registro de pagamento de mensalidade**
Como filho da casa, quero solicitar a baixa no pagamento mensal para constar a regularidade.
- Precisa estar logado;
- Pode enviar comprovante (imagem ou PDF);
- Aceito mediante avaliação de um ADM;

**MUST-04 // Listagem de regularidade dos membros**
Como ADM, quero visualizar a situação dos filhos para estimar o valor pendente a receber no mês.
- Funcionalidade disponível apenas para ADM;
- Painel com lista de inadimplentes e isentos do mês;

**MUST-05 // Avaliação de pagamentos**
Como ADM, quero dar baixa na solicitação de pagamento de um filho para garantir que o relatório esteja atualizado.
- Funcionalidade disponível apenas para ADM;
- Aprovação ou recusa mediante visualização do comprovante;

**MUST-06 // Alteração no tipo de perfil**
Como ADM, quero alterar o tipo de conta de um membro.
- Funcionalidade disponível apenas para ADM;
- Confirmação solicitada antes de salvar;

**NICE-01 // Extrato financeiro**
Como filho da casa ou ADM, quero acessar um extrato de movimentações para ter clareza sobre o destino dos valores arrecadados.

**NICE-02 // Movimentação financeira**
Como ADM, quero registrar uma movimentação de entrada ou saída de caixa para atualizar o extrato financeiro.

**NICE-03 // Isenção mensal**
Como ADM, quero isentar um filho do mês corrente para que ele não apareça como inadimplente no painel.

## Mapa do site

```text
/                        → redireciona para /login/
/login/                  → pública
/logout/                 → encerra sessão
/home/                   → protegida — dashboard principal
/filhos/                 → somente ADM
│  ├── /filhos/cadastrar/
│  └── /filhos/<pk>/editar/
│  └── /filhos/<pk>/excluir/
/mensalidades/           → todos os usuários logados
│  └── /mensalidades/registrar/
│  ├── /mensalidades/<pk>/aprovar/   → somente ADM
│  ├── /mensalidades/<pk>/negar/     → somente ADM
│  └── /mensalidades/<pk>/excluir/   → somente ADM
/financeiro/             → todos os usuários logados
│  ├── /financeiro/registrar/        → somente ADM
│  └── /financeiro/<pk>/excluir/     → somente ADM
/perfil/                 → todos os usuários logados
```

## Wireframes

> _Prints das telas serão adicionados em breve._

## Stack técnica

| Camada | Tecnologia |
|---|---|
| Back-end | Python 3.10 / Django 5.2 |
| Front-end | Bootstrap 5.3 / Bootstrap Icons |
| Banco de dados | PostgreSQL |
| API REST | Django REST Framework + SimpleJWT |
| Arquivos estáticos | WhiteNoise |
| Deploy | Railway |
| Versionamento | GitHub |

## Fontes de dados

Os dados são cadastrados manualmente pelos ADMs diretamente no sistema. Armazenados em banco PostgreSQL provisionado via Railway.

## Documentação técnica

A documentação detalhada de cada funcionalidade está em [`/docs`](docs/index.md).

## Riscos e atenções

- O sistema não realiza validação de CPF; é importante que os ADMs confiram os dados no momento do cadastro;
- Para que os relatórios se mantenham fiéis, os ADMs devem verificar constantemente as solicitações de pagamento pendentes;
- Membros comuns não têm acesso às informações pessoais dos demais membros;
- A exclusão de um filho remove em cascata todas as suas mensalidades — a operação é irreversível;

## Cronograma pessoal

**25/05/2026**
- Criação de repositório no GitHub;
- Início do documento para entrega;
- Branch "roteiro" criada;
- Adequação de textos pré-existentes;

**26/05/2026**
- Desenvolvimento dos tópicos a serem entregues:
  - Listagem de funcionalidades;
  - Mapa do site;
  - Criação de wireframes no Figma;
  - Stack técnica;
  - Fonte de dados;
  - Cronograma pessoal;
- Conteúdos do roteiro adicionados e commitados;
