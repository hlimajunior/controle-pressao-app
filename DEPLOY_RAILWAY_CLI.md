# Deploy Permanente no Railway.app - Guia Passo a Passo

## ✨ O que você vai conseguir

Ao final deste guia, sua aplicação estará rodando permanentemente em:

-   URL pública e permanente (ex: `controle-pressao-app-production.up.railway.app`)
-   SSL/HTTPS automático
-   Deploy automático a cada atualização
-   **100% GRATUITO** (Railway oferece $5 de crédito por mês no plano gratuito)

---

## 📋 Pré-requisitos

1. **Node.js instalado** (para instalar o Railway CLI)

    - Verifique: `node --version`
    - Se não tiver, baixe em: https://nodejs.org

2. **Conta no Railway.app**
    - Acesse: https://railway.app
    - Clique em "Sign in" e faça login com GitHub, Google ou Email

---

## 🚀 Passo a Passo para Deploy

### Passo 1: Instalar o Railway CLI

Abra o terminal/prompt de comando e execute:

```bash
npm install -g @railway/cli
```

Aguarde a instalação completar (leva cerca de 1 minuto).

### Passo 2: Fazer Login no Railway

No terminal, execute:

```bash
railway login
```

Isso abrirá uma página no navegador para você autorizar o acesso. Clique em **"Authorize"**.

### Passo 3: Navegar até a Pasta do Projeto

```bash
cd controle-pressao-app
```

### Passo 4: Inicializar o Projeto no Railway

```bash
railway init
```

Você verá algumas perguntas:

-   **"What would you like to do?"** → Escolha **"Create a new project"**
-   **"Enter project name"** → Digite: `controle-pressao-app` (ou o nome que preferir)

### Passo 5: Fazer o Deploy

```bash
railway up
```

Aguarde o upload dos arquivos (leva cerca de 30 segundos).

### Passo 6: Gerar URL Pública

```bash
railway domain
```

Isso gerará uma URL pública para sua aplicação. Você verá algo como:

```
✓ Domain created: controle-pressao-app-production.up.railway.app
```

### Passo 7: Abrir a Aplicação

```bash
railway open
```

Isso abrirá automaticamente sua aplicação no navegador! 🎉

---

## 🔧 Comandos Úteis

### Ver logs da aplicação

```bash
railway logs
```

### Ver status do deploy

```bash
railway status
```

### Redeployar após fazer mudanças

```bash
railway up
```

### Abrir dashboard do Railway

```bash
railway open
```

### Ver variáveis de ambiente

```bash
railway variables
```

---

## 📊 Configurar Google Sheets (Opcional)

Se você quiser usar a funcionalidade de exportação para Google Sheets:

### Opção 1: Via Dashboard Web

1. Execute: `railway open`
2. Vá em **"Variables"**
3. Clique em **"New Variable"**
4. Adicione:
    - **Name**: `GOOGLE_APPLICATION_CREDENTIALS_JSON`
    - **Value**: Cole todo o conteúdo do arquivo `credentials.json`

### Opção 2: Via CLI

```bash
railway variables set GOOGLE_APPLICATION_CREDENTIALS_JSON="$(cat credentials.json)"
```

Depois, você precisará modificar o código para ler as credenciais dessa variável de ambiente.

---

## 💰 Sobre o Plano Gratuito

O Railway oferece:

-   **$5 de crédito por mês** no plano gratuito
-   Isso é suficiente para rodar uma aplicação pequena/média 24/7
-   Sem necessidade de cartão de crédito
-   Se ultrapassar o limite, a aplicação para até o próximo ciclo

**Dica**: Para economizar créditos, a aplicação entra em "sleep mode" após 15 minutos de inatividade e acorda automaticamente no próximo acesso.

---

## 🔄 Atualizando a Aplicação

Sempre que você fizer mudanças no código:

```bash
cd controle-pressao-app
railway up
```

O Railway fará o deploy automaticamente da nova versão!

---

## ❓ Solução de Problemas

### Erro: "railway: command not found"

Reinstale o Railway CLI:

```bash
npm install -g @railway/cli
```

### Erro: "No project found"

Execute novamente:

```bash
railway init
```

### Aplicação não está funcionando

Veja os logs:

```bash
railway logs
```

### Erro de porta

O Railway define automaticamente a variável `PORT`. O código já está configurado para usar essa variável.

---

## 📞 Precisa de Ajuda?

Se tiver qualquer problema durante o deploy, me avise em qual passo está e qual erro apareceu!

---

## ✅ Checklist de Deploy

-   [ ] Node.js instalado
-   [ ] Conta criada no Railway.app
-   [ ] Railway CLI instalado (`npm install -g @railway/cli`)
-   [ ] Login feito (`railway login`)
-   [ ] Projeto inicializado (`railway init`)
-   [ ] Deploy realizado (`railway up`)
-   [ ] Domínio gerado (`railway domain`)
-   [ ] Aplicação testada e funcionando

---

**Tempo estimado total**: 5-10 minutos

**Custo**: R$ 0,00 (100% gratuito)

Boa sorte com o deploy! 🚀
