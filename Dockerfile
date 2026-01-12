# Python exatamente na versão exigida
FROM python:3.12.12-slim-bookworm

# Variáveis de ambiente (boas práticas)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências de sistema mínimas
RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Instala o uv
RUN pip install --no-cache-dir uv

# Copia apenas arquivos de dependências (cache eficiente)
COPY pyproject.toml uv.lock* ./

# Instala dependências (sem dev)
RUN uv sync --frozen --no-dev

# Copia o restante da aplicação
COPY . .

# Cria usuário não-root (segurança)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Porta do Flask/Gunicorn
EXPOSE 5000

# Comando de inicialização
CMD ["uv", "run", "gunicorn", "-b", "0.0.0.0:5000", "app:app"]
