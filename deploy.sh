#!/bin/bash

# Script automatizado para deploy no Railway.app
# Autor: Manus AI
# Data: 2024

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     Deploy Automático - Controle de Pressão Arterial       ║"
echo "║                 Railway.app                                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para verificar se comando existe
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Passo 1: Verificar Node.js
echo -e "${YELLOW}[1/6]${NC} Verificando Node.js..."
if command_exists node; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓${NC} Node.js instalado: $NODE_VERSION"
else
    echo -e "${RED}✗${NC} Node.js não encontrado!"
    echo "Por favor, instale o Node.js: https://nodejs.org"
    exit 1
fi
echo ""

# Passo 2: Verificar/Instalar Railway CLI
echo -e "${YELLOW}[2/6]${NC} Verificando Railway CLI..."
if command_exists railway; then
    RAILWAY_VERSION=$(railway --version)
    echo -e "${GREEN}✓${NC} Railway CLI instalado: $RAILWAY_VERSION"
else
    echo -e "${YELLOW}⚠${NC} Railway CLI não encontrado. Instalando..."
    npm install -g @railway/cli
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} Railway CLI instalado com sucesso!"
    else
        echo -e "${RED}✗${NC} Erro ao instalar Railway CLI"
        exit 1
    fi
fi
echo ""

# Passo 3: Verificar autenticação
echo -e "${YELLOW}[3/6]${NC} Verificando autenticação no Railway..."
railway whoami >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Você já está autenticado no Railway!"
else
    echo -e "${YELLOW}⚠${NC} Você precisa fazer login no Railway"
    echo "Abrindo página de login..."
    railway login
    if [ $? -ne 0 ]; then
        echo -e "${RED}✗${NC} Erro ao fazer login"
        exit 1
    fi
    echo -e "${GREEN}✓${NC} Login realizado com sucesso!"
fi
echo ""

# Passo 4: Inicializar projeto
echo -e "${YELLOW}[4/6]${NC} Inicializando projeto no Railway..."
if [ -f ".railway/config.json" ]; then
    echo -e "${GREEN}✓${NC} Projeto já está inicializado"
else
    echo "Criando novo projeto..."
    railway init --name controle-pressao-app
    if [ $? -ne 0 ]; then
        echo -e "${RED}✗${NC} Erro ao inicializar projeto"
        exit 1
    fi
    echo -e "${GREEN}✓${NC} Projeto inicializado!"
fi
echo ""

# Passo 5: Deploy
echo -e "${YELLOW}[5/6]${NC} Fazendo deploy da aplicação..."
railway up
if [ $? -ne 0 ]; then
    echo -e "${RED}✗${NC} Erro ao fazer deploy"
    exit 1
fi
echo -e "${GREEN}✓${NC} Deploy realizado com sucesso!"
echo ""

# Passo 6: Gerar domínio
echo -e "${YELLOW}[6/6]${NC} Gerando URL pública..."
railway domain 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠${NC} Tentando gerar domínio..."
    railway domain
fi
echo ""

# Finalização
echo "╔════════════════════════════════════════════════════════════╗"
echo "║              🎉 DEPLOY CONCLUÍDO COM SUCESSO! 🎉          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}Sua aplicação está rodando!${NC}"
echo ""
echo "Comandos úteis:"
echo "  • Ver logs:      railway logs"
echo "  • Abrir app:     railway open"
echo "  • Ver status:    railway status"
echo "  • Redeploy:      railway up"
echo ""
echo -e "${YELLOW}Abrindo aplicação no navegador...${NC}"
sleep 2
railway open
