
🚀 Projeto Django 6.0 com UV
Documentação Oficial: https://docs.djangoproject.com/en/6.0/

🛠️ 1. Configuração do Ambiente (UV)
O uv é a ferramenta moderna para gerir o Python e as dependências de forma isolada e rápida.

# Inicializa o ficheiro de configuração pyproject.toml na raiz
uv init

# Cria a pasta .venv (ambiente virtual) de forma explícita (opcional, pois o add já faz isso)
uv venv

# Instala a versão específica do Python 3.14 no projeto
uv install python 3.14

# Fixa (pina) o projeto à versão 3.14 para garantir consistência entre desenvolvedores
uv python pin 3.14

# Adiciona o Django e o Uvicorn (servidor ASGI para performance e async) às dependências
uv add uvicorn django

# Sincroniza o ambiente para garantir que todas as libs instaladas estão corretas
uv sync




2. Inicialização do Framework Django
O Django possui uma estrutura de "Projeto" (casca principal) e "Apps" (funcionalidades específicas).

# COMANDO CRUCIAL: Cria o projeto core na pasta atual
# O ponto '.' no final evita que o Django crie pastas duplicadas/redundantes
uv run django-admin startproject django_project .

# Para consultar todas as ferramentas e comandos disponíveis no django-admin:
uv run django-admin --help

# Cria um novo módulo (App). Use nomes no plural para representar coleções de dados
# Exemplo: 'meetings' para gerir uma lista de reuniões
uv run python manage.py startapp meetings



Gestão de Containers e Limpeza (Docker)
Comandos úteis para gerir o ambiente e evitar conflitos de portas (como a 8000) com outros serviços:


# Lista todos os containers que estão em execução no momento
docker ps

# Para todos os containers ativos no sistema (limpeza total de processos antigos)
docker stop $(docker ps -aq)


🚀 Como Executar o Projeto
Para iniciar o servidor de desenvolvimento localmente, utilize:

uv run python manage.py runserver



📂 Estrutura e Gestão do Projeto
manage.py: O ficheiro mais importante do projeto. Não devemos mexer nele. Ele é o motor que executa comandos como iniciar o servidor, criar migrações e gerir a base de dados.

django_project/: Pasta com o nome do projeto (podia ser qualquer nome, como 'bananas'). Contém os ficheiros vitais para o projeto arrancar, como settings.py (configurações) e urls.py (rotas).

.venv/: Pasta do ambiente virtual. Contém o interpretador e as bibliotecas. Deve ser sempre ignorada no Git.
