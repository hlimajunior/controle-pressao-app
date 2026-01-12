#!/bin/bash

# Script para iniciar a aplicação de controle de controles

echo "Iniciando aplicação de Controle de Pressão Arterial..."

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se o banco de dados existe, caso contrário criar
if [ ! -f controles.db ]; then
    echo "Criando banco de dados..."
    python -c "from app import app, db; app.app_context().push(); db.create_all()"
fi

# Iniciar aplicação
echo "Servidor iniciando em http://localhost:12080"
python app.py
