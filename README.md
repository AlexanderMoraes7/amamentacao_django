# 🤱 Suporte à Amamentação

Aplicação web desenvolvida em Django para apoio à amamentação, conectando mães doadoras de leite materno a unidades de coleta e fornecendo informações e suporte à comunidade.

> **Projeto Integrador — Primeira Entrega**  
> Curso de Análise e Desenvolvimento de Sistemas

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Requisitos de Negócio](#requisitos-de-negócio)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Usar](#como-usar)
- [Modelos de Dados](#modelos-de-dados)
- [Rotas da Aplicação](#rotas-da-aplicação)

---

## Sobre o Projeto

O **Suporte à Amamentação** é uma plataforma digital voltada para facilitar a doação de leite materno e promover a cultura da amamentação. A aplicação conecta mães doadoras a bancos de leite humano (BLH) e unidades de saúde, além de oferecer informações educativas sobre amamentação.

O projeto foi desenvolvido como Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas, com foco em atender às necessidades de mães, profissionais de saúde e unidades de coleta de leite materno.

---

## Requisitos de Negócio

Com base no documento de requisitos da primeira entrega, os seguintes requisitos de negócio foram identificados:

### 🎯 Objetivo Geral
Desenvolver uma aplicação web que facilite a doação de leite materno, conectando doadoras a unidades de saúde e promovendo a amamentação por meio de informações e suporte à comunidade.

### 👥 Atores do Sistema
- **Mãe Doadora** — usuária que deseja cadastrar-se para doar leite materno
- **Mãe Receptora** — usuária que busca informações sobre bancos de leite
- **Administrador** — responsável pela gestão da plataforma

### 📌 Requisitos Funcionais

| ID | Requisito |
|----|-----------|
| RF01 | O sistema deve permitir o cadastro de novos usuários com nome de usuário, e-mail e senha |
| RF02 | O sistema deve autenticar usuários por meio de login com usuário e senha |
| RF03 | O sistema deve permitir a recuperação de conta/senha |
| RF04 | O sistema deve permitir que o usuário edite seu perfil (nome, e-mail, endereço e foto) |
| RF05 | O sistema deve exibir um feed principal com conteúdo relevante sobre amamentação |
| RF06 | O sistema deve permitir que usuários se cadastrem como doadoras de leite materno |
| RF07 | O sistema deve exibir informações educativas sobre amamentação |
| RF08 | O sistema deve listar unidades de coleta de leite materno (Bancos de Leite Humano) |
| RF09 | O sistema deve possuir uma área de configurações do usuário |
| RF10 | O sistema deve exibir notificações ao usuário |

### 📌 Requisitos Não Funcionais

| ID | Requisito |
|----|-----------|
| RNF01 | A aplicação deve ser desenvolvida em Django (Python) |
| RNF02 | A interface deve ser responsiva e adaptada para dispositivos móveis |
| RNF03 | O sistema deve ser desenvolvido em português (pt-BR) |
| RNF04 | As senhas dos usuários devem ser armazenadas de forma segura (hash) |
| RNF05 | O sistema deve utilizar banco de dados relacional |
| RNF06 | Arquivos de mídia enviados pelos usuários devem ser gerenciados de forma segura |
| RNF07 | Rotas protegidas devem exigir autenticação do usuário |

### 🗂️ Regras de Negócio

- Apenas usuários autenticados podem acessar as funcionalidades principais da plataforma
- O e-mail é obrigatório no cadastro de usuário
- Ao atualizar a foto de perfil, a imagem anterior deve ser removida do servidor
- O cadastro como doadora requer que o usuário esteja autenticado
- As unidades de coleta de leite são gerenciadas pelo administrador da plataforma

---

## Funcionalidades

### ✅ Implementadas
- [x] Cadastro de usuário (username, e-mail, senha)
- [x] Login e logout
- [x] Perfil do usuário com foto, nome, e-mail e endereço
- [x] Upload e gerenciamento de foto de perfil
- [x] Navegação entre seções via barra inferior
- [x] Proteção de rotas com autenticação obrigatória

### 🚧 Em Desenvolvimento
- [ ] Feed principal com conteúdo
- [ ] Cadastro de doadora de leite
- [ ] Listagem de unidades de coleta (BLH)
- [ ] Informações educativas sobre amamentação
- [ ] Configurações do usuário
- [ ] Recuperação de conta/senha
- [ ] Sistema de notificações

---

## Tecnologias

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.x | Linguagem principal |
| Django | 5.2.5 | Framework web |
| SQLite / PostgreSQL | — | Banco de dados |
| HTML5 / CSS3 | — | Frontend |
| JavaScript | — | Interatividade |
| Font Awesome | 6.5.2 | Ícones |
| python-decouple | — | Variáveis de ambiente |
| dj-database-url | — | Configuração de banco de dados |
| Pillow | — | Processamento de imagens |

---

## Estrutura do Projeto

```
amamentacao_django/
│
├── app/                        # Configuração principal do projeto
│   ├── settings.py             # Configurações do Django
│   ├── urls.py                 # Roteamento principal
│   ├── templates/              # Templates base e de cada módulo
│   │   ├── base.html           # Template base com navegação
│   │   ├── login.html
│   │   ├── accounts.html
│   │   ├── profiles.html
│   │   ├── feed.html
│   │   ├── settings.html
│   │   ├── informations.html
│   │   ├── be_a_donor.html
│   │   ├── units.html
│   │   └── account_recovery.html
│   └── templatetags/
│       └── ensure_overridden.py
│
├── accounts/                   # Cadastro de usuários
│   ├── views.py
│   └── forms.py
│
├── login/                      # Autenticação
│   └── views.py
│
├── account_recovery/           # Recuperação de conta
│   └── views.py
│
├── profiles/                   # Perfil do usuário
│   ├── models.py               # Photo, Address
│   ├── views.py
│   ├── forms.py
│   └── migrations/
│
├── feed/                       # Feed principal
│   └── views.py
│
├── settings/                   # Configurações do usuário
│   └── views.py
│
├── informations/               # Informações sobre amamentação
│   └── views.py
│
├── be_a_donor/                 # Cadastro de doadoras
│   └── views.py
│
├── units/                      # Unidades de coleta de leite
│   └── views.py
│
├── static/                     # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   └── js/
│
├── media/                      # Arquivos enviados pelos usuários
│   └── profiles/
│
├── manage.py
├── pyproject.toml
└── poetry.lock
```

---

## Instalação e Configuração

### Pré-requisitos
- Python 3.10+
- pip ou Poetry

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd amamentacao_django
```

### 2. Crie e ative o ambiente virtual

```bash
# Com venv
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/macOS

# Ou com Poetry
poetry install
poetry shell
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
# ou
poetry install
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Como Usar

1. **Cadastro**: Acesse `/accounts/` para criar uma nova conta informando usuário, e-mail e senha.
2. **Login**: Acesse `/login/` para entrar na plataforma.
3. **Feed**: Após o login, você será redirecionado para o feed principal.
4. **Perfil**: Clique no ícone de usuário na barra inferior para editar seu perfil, foto e endereço.
5. **Navegação**: Use a barra inferior para acessar as seções: Informações, Seja Doadora, Feed, Unidades e Perfil.

---

## Modelos de Dados

### Photo
| Campo | Tipo | Descrição |
|-------|------|-----------|
| user | OneToOneField (User) | Usuário dono da foto |
| path_image | ImageField | Caminho da imagem de perfil |

### Address
| Campo | Tipo | Descrição |
|-------|------|-----------|
| user | OneToOneField (User) | Usuário dono do endereço |
| user_address | TextField | Endereço do usuário |

---

## Rotas da Aplicação

| URL | View | Descrição | Auth |
|-----|------|-----------|------|
| `/admin/` | Django Admin | Painel administrativo | Sim |
| `/accounts/` | accounts_view | Cadastro de usuário | Não |
| `/login/` | login_view | Login | Não |
| `/logout/` | logout_view | Logout | Sim |
| `/account_recovery/` | account_recovery_view | Recuperação de conta | Sim |
| `/feed/` | feed_view | Feed principal | Sim |
| `/settings/` | settings_view | Configurações | Sim |
| `/informations/` | informations_view | Informações | Sim |
| `/be_a_donor/` | be_a_donor_view | Seja doadora | Sim |
| `/units/` | units_view | Unidades de coleta | Sim |
| `/profiles/` | profiles_view | Perfil do usuário | Sim |

---

## 👥 Equipe

Projeto desenvolvido como trabalho acadêmico do curso de Análise e Desenvolvimento de Sistemas.

---

## 📄 Licença

Este projeto é de uso acadêmico. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
