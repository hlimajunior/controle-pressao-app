# Guia de Deploy - Controle de Despesas

## Opções de Hospedagem Gratuita

### Opção 1: PythonAnywhere (Recomendado - Mais Simples)

**Vantagens**: Muito fácil, suporta SQLite nativamente, interface amigável

**Passos**:

1. Acesse [PythonAnywhere](https://www.pythonanywhere.com) e crie uma conta gratuita
2. No Dashboard, vá em **"Web"** > **"Add a new web app"**
3. Escolha **"Flask"** e **"Python 3.10"**
4. Faça upload dos arquivos do projeto:
    - Vá em **"Files"**
    - Navegue até `/home/seu_usuario/mysite/`
    - Faça upload de todos os arquivos do projeto
5. Configure o arquivo WSGI:
    - Vá em **"Web"** > **"WSGI configuration file"**
    - Substitua o conteúdo pelo seguinte:

```python
import sys
import os

# Adicionar o diretório do projeto ao path
project_home = '/home/seu_usuario/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Importar a aplicação Flask
from app import app as application
```

6. Instale as dependências:

    - Vá em **"Consoles"** > **"Bash"**
    - Execute:

    ```bash
    cd mysite
    pip3 install --user -r requirements.txt
    ```

7. Clique em **"Reload"** no painel Web
8. Acesse sua aplicação em: `seu_usuario.pythonanywhere.com`

---

### Opção 2: Railway.app

**Vantagens**: Deploy automático via GitHub, muito moderno

**Passos**:

1. Primeiro, você precisa criar um repositório no GitHub:

    - Acesse [GitHub](https://github.com) e faça login
    - Clique em **"New repository"**
    - Nome: `controle-pressao-app`
    - Marque como **Public**
    - Clique em **"Create repository"**

2. No seu computador, faça upload do código:

    ```bash
    cd controle-pressao-app
    git remote add origin https://github.com/SEU_USUARIO/controle-pressao-app.git
    git branch -M main
    git push -u origin main
    ```

3. Acesse [Railway.app](https://railway.app) e faça login com GitHub
4. Clique em **"New Project"** > **"Deploy from GitHub repo"**
5. Selecione o repositório `controle-pressao-app`
6. Railway detectará automaticamente que é uma aplicação Python
7. Aguarde o deploy (leva cerca de 2-3 minutos)
8. Clique em **"Settings"** > **"Generate Domain"** para obter a URL pública

---

### Opção 3: Render.com

**Vantagens**: Muito confiável, SSL grátis, fácil configuração

**Passos**:

1. Primeiro, crie um repositório no GitHub (mesmos passos da Opção 2, item 1 e 2)

2. Acesse [Render.com](https://render.com) e faça login com GitHub
3. Clique em **"New +"** > **"Web Service"**
4. Conecte seu repositório GitHub `controle-pressao-app`
5. Configure:
    - **Name**: `controle-pressao-app`
    - **Environment**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`
    - **Plan**: `Free`
6. Clique em **"Create Web Service"**
7. Aguarde o deploy (leva cerca de 5 minutos)
8. Sua aplicação estará disponível em: `controle-pressao-app.onrender.com`

**Nota**: No plano gratuito do Render, a aplicação "dorme" após 15 minutos de inatividade e leva ~30 segundos para "acordar" no primeiro acesso.

---

### Opção 4: Koyeb

**Vantagens**: Rápido, moderno, bom uptime

**Passos**:

1. Crie um repositório no GitHub (mesmos passos da Opção 2)
2. Acesse [Koyeb](https://www.koyeb.com) e crie uma conta
3. Clique em **"Create App"**
4. Escolha **"GitHub"** e conecte seu repositório
5. Configure:
    - **Builder**: `Buildpack`
    - **Run command**: `gunicorn app:app`
    - **Port**: `8000`
6. Clique em **"Deploy"**
7. Aguarde o deploy completar

---

## Arquivos Necessários para Deploy

Todos os arquivos já estão preparados no projeto:

-   ✅ `requirements.txt` - Dependências Python
-   ✅ `Procfile` - Comando para iniciar a aplicação
-   ✅ `runtime.txt` - Versão do Python
-   ✅ `app.py` - Configurado para produção
-   ✅ `.gitignore` - Ignora arquivos sensíveis

---

## Configuração do Google Sheets no Servidor

Após fazer o deploy, para configurar a exportação para Google Sheets:

### No PythonAnywhere:

1. Vá em **"Files"**
2. Faça upload do arquivo `credentials.json` para a pasta do projeto
3. Certifique-se de que o arquivo está no mesmo diretório que `app.py`

### No Railway/Render/Koyeb:

1. Vá nas configurações do projeto
2. Adicione uma **Environment Variable**:
    - Nome: `GOOGLE_CREDENTIALS`
    - Valor: Cole todo o conteúdo do arquivo `credentials.json`
3. Modifique o código para ler as credenciais da variável de ambiente

---

## Recomendação Final

Para **facilidade máxima**: Use **PythonAnywhere** (não precisa de Git/GitHub)

Para **melhor experiência**: Use **Railway.app** ou **Render.com** (deploy automático via GitHub)

---

## Precisa de Ajuda?

Se tiver dificuldades, me avise qual opção você escolheu e em qual passo está com problemas!
