#!/bin/bash

# Script para deploy no Railway.app

echo "==================================="
echo "Deploy no Railway.app"
echo "==================================="
echo ""

# Verificar se Railway CLI está instalado
if ! command -v railway &> /dev/null; then
    echo "Instalando Railway CLI..."
    npm install -g @railway/cli
fi

echo "Para fazer o deploy no Railway, siga os passos:"
echo ""
echo "1. Execute: railway login"
echo "2. Execute: railway init"
echo "3. Execute: railway up"
echo ""
echo "Ou acesse: https://railway.app e faça o deploy via interface web"
echo ""
echo "Documentação: https://docs.railway.app/deploy/deployments"
