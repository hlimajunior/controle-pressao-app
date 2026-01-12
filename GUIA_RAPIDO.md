# Guia Rápido - Controle de Pressão Arterial

## Como Iniciar a Aplicação

### Opção 1: Usando o script automático

```bash
cd controle-pressao-app
./start.sh
```

### Opção 2: Manualmente

```bash
cd controle-pressao-app
source venv/bin/activate
python app.py
```

A aplicação estará disponível em: **http://localhost:12080**

## Como Usar

### 1. Adicionar uma Controle

1. Clique no botão **"Nova Controle"** ou acesse o menu **"Adicionar"**
2. Preencha os campos:
    - **Descrição**: Nome da controle (ex: "Almoço no restaurante")
    - **Valor**: Valor em reais (ex: 45.50)
    - **Data**: Data da medição
    - **Observações**: Informações adicionais (opcional)
3. Clique em **"Salvar Controle"**

### 2. Visualizar Medições

-   A página inicial mostra todas as controles cadastradas
-   O **total de controles** é exibido no canto superior direito
-   As controles são ordenadas da mais recente para a mais antiga

### 3. Editar uma Controle

1. Na lista de controles, clique no ícone de **edição** (lápis)
2. Modifique os campos desejados
3. Clique em **"Atualizar Controle"**

### 4. Excluir uma Controle

1. Na lista de controles, clique no ícone de **exclusão** (lixeira)
2. Confirme a exclusão na mensagem que aparecer

### 5. Exportar para Google Sheets

#### Configuração Inicial (necessária apenas uma vez)

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto e ative as APIs:
    - Google Sheets API
    - Google Drive API
3. Crie uma **Conta de Serviço** e baixe o arquivo JSON
4. Renomeie o arquivo para `credentials.json` e coloque na pasta `controle-pressao-app`
5. Copie o email da conta de serviço (está dentro do arquivo `credentials.json`)
6. No Google Sheets, compartilhe sua planilha com esse email (permissão de Editor)

#### Exportando os Dados

1. Na página inicial, clique em **"Exportar para Google Sheets"**
2. Digite o nome da planilha (deve ser exatamente o mesmo nome da planilha no Google Sheets)
3. Clique em **"Exportar"**
4. Os dados serão enviados para a planilha

## Dicas

-   **Data padrão**: Ao adicionar uma medição, a data atual é preenchida automaticamente
-   **Formato de valor**: Use ponto ou vírgula como separador decimal (ex: 45.50 ou 45,50)
-   **Observações**: Use este campo para adicionar detalhes como forma de pagamento, parcelas, etc.
-   **Backup**: Exporte regularmente para Google Sheets para ter um backup dos seus dados

## Solução Rápida de Problemas

### A aplicação não inicia

```bash
# Verifique se o ambiente virtual está ativo
source venv/bin/activate

# Reinstale as dependências
pip install -r requirements.txt
```

### Erro ao exportar para Google Sheets

-   Verifique se o arquivo `credentials.json` está na pasta raiz
-   Verifique se a planilha foi compartilhada com o email correto
-   Certifique-se de que o nome da planilha está correto

### Porta 5000 já está em uso

```bash
# Mate o processo na porta 5000
fuser -k 5000/tcp

# Ou edite app.py e mude a porta para outra (ex: 5001)
```

## Atalhos de Teclado

-   **Tab**: Navegar entre campos do formulário
-   **Enter**: Submeter formulário (quando em um campo de input)
-   **Esc**: Fechar modal de exportação

## Acesso via Rede Local

Para acessar a aplicação de outros dispositivos na mesma rede:

1. Descubra seu IP local:

    ```bash
    ip addr show | grep inet
    ```

2. Acesse de outro dispositivo usando:
    ```
    http://SEU_IP:12080
    ```

---

**Precisa de mais ajuda?** Consulte o arquivo `README.md` para documentação completa.
