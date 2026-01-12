# Deploy no Windows - Guia Simplificado

## Para usuários do Windows

Se você está usando Windows, siga estes passos:

### 1. Instalar Node.js

1. Baixe o Node.js em: https://nodejs.org
2. Execute o instalador e siga as instruções
3. Reinicie o computador após a instalação

### 2. Abrir o Prompt de Comando

1. Pressione `Win + R`
2. Digite `cmd` e pressione Enter

### 3. Instalar Railway CLI

No Prompt de Comando, execute:

```cmd
npm install -g @railway/cli
```

### 4. Navegar até a pasta do projeto

```cmd
cd caminho\para\controle-pressao-app
```

**Dica**: Você pode arrastar a pasta para o Prompt de Comando para obter o caminho automaticamente.

### 5. Fazer Login no Railway

```cmd
railway login
```

Isso abrirá o navegador. Faça login e autorize.

### 6. Inicializar Projeto

```cmd
railway init
```

Escolha:

-   "Create a new project"
-   Digite o nome: `controle-pressao-app`

### 7. Fazer Deploy

```cmd
railway up
```

### 8. Gerar URL Pública

```cmd
railway domain
```

### 9. Abrir a Aplicação

```cmd
railway open
```

---

## Alternativa: PowerShell

Se preferir usar o PowerShell:

1. Pressione `Win + X` e escolha "Windows PowerShell"
2. Execute os mesmos comandos acima (funcionam igual)

---

## Alternativa: Interface Gráfica (Mais Fácil)

Se você preferir não usar linha de comando:

1. Acesse: https://railway.app
2. Faça login
3. Clique em "New Project"
4. Escolha "Deploy from GitHub repo"
5. Conecte sua conta do GitHub
6. Crie um novo repositório e faça upload dos arquivos
7. Selecione o repositório
8. Railway fará o deploy automaticamente

---

## Precisa de Ajuda?

Se tiver dificuldades, me avise qual erro está aparecendo!
