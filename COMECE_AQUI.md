# 🚀 COMECE AQUI - Deploy Permanente

## Escolha seu método de deploy:

### ⚡ Método Rápido (Recomendado)

**Para Linux/Mac:**

```bash
cd controle-pressao-app
./deploy.sh
```

**Para Windows:**

```cmd
cd controle-pressao-app
railway login
railway init
railway up
railway domain
railway open
```

---

### 📖 Guias Detalhados

Escolha o guia adequado para você:

1. **DEPLOY_RAILWAY_CLI.md** - Guia completo passo a passo (Linux/Mac/Windows)
2. **DEPLOY_WINDOWS.md** - Guia específico para Windows
3. **DEPLOY.md** - Todas as opções de hospedagem disponíveis

---

### 🎯 Resumo Ultra-Rápido

1. Instale Node.js: https://nodejs.org
2. Abra o terminal na pasta `controle-pressao-app`
3. Execute:
    ```bash
    npm install -g @railway/cli
    railway login
    railway init
    railway up
    railway domain
    ```
4. Pronto! Sua aplicação está no ar! 🎉

---

### ❓ Precisa de Ajuda?

-   **Erro no deploy?** Veja os logs: `railway logs`
-   **Não tem Node.js?** Baixe em: https://nodejs.org
-   **Prefere interface gráfica?** Acesse: https://railway.app

---

### 📁 Arquivos Importantes

-   `app.py` - Aplicação principal
-   `requirements.txt` - Dependências Python
-   `Procfile` - Comando de inicialização
-   `deploy.sh` - Script automatizado de deploy (Linux/Mac)

---

**Tempo estimado de deploy: 5 minutos**

**Custo: R$ 0,00 (100% gratuito)**

Boa sorte! 🍀
