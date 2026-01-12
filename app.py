from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Controle
from config import Config
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from sqlalchemy import text


app = Flask(__name__)
app.config.from_object(Config)

# Inicializar banco de dados
db.init_app(app)

# Criar tabelas
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    """Página principal com listagem de controles"""
    controles = Controle.query.order_by(
        Controle.data.desc(), Controle.hora.desc()).all()

    return render_template("index.html", controles=controles)


@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    """Adicionar novo controle"""
    if request.method == "POST":
        try:
            data_str = request.form.get("data")
            hora_str = request.form.get("hora")
            sistolica = int(request.form.get("sistolica"))
            diastolica = int(request.form.get("diastolica"))
            frequencia_str = request.form.get("frequencia")
            observacoes = request.form.get("observacoes")

            # Converter string de data para objeto date
            data = datetime.strptime(data_str, "%Y-%m-%d").date()

            # Converter string de hora para objeto time
            hora = datetime.strptime(hora_str, "%H:%M").time()

            # Converter frequência (pode ser vazio)
            frequencia = int(frequencia_str) if frequencia_str else None

            # Criar novo controle
            novo_controle = Controle(
                data=data,
                hora=hora,
                sistolica=sistolica,
                diastolica=diastolica,
                frequencia=frequencia,
                observacoes=observacoes,
            )

            db.session.add(novo_controle)
            db.session.commit()

            flash("Medição adicionada com sucesso!", "success")
            return redirect(url_for("index"))

        except Exception as e:
            flash(f"Erro ao adicionar medição: {str(e)}", "error")
            return redirect(url_for("adicionar"))

    return render_template("adicionar.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    """Editar controle existente"""
    controle = Controle.query.get_or_404(id)

    if request.method == "POST":
        try:
            data_str = request.form.get("data")
            hora_str = request.form.get("hora")
            controle.sistolica = int(request.form.get("sistolica"))
            controle.diastolica = int(request.form.get("diastolica"))
            frequencia_str = request.form.get("frequencia")
            controle.observacoes = request.form.get("observacoes")

            controle.data = datetime.strptime(data_str, "%Y-%m-%d").date()
            controle.hora = datetime.strptime(hora_str, "%H:%M").time()
            controle.frequencia = int(
                frequencia_str) if frequencia_str else None

            db.session.commit()

            flash("Medição atualizada com sucesso!", "success")
            return redirect(url_for("index"))

        except Exception as e:
            flash(f"Erro ao atualizar medição: {str(e)}", "error")
            return redirect(url_for("editar", id=id))

    return render_template("editar.html", controle=controle)


@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    """Excluir controle"""
    try:
        controle = Controle.query.get_or_404(id)
        db.session.delete(controle)
        db.session.commit()

        flash("Medição excluída com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao excluir medição: {str(e)}", "error")

    return redirect(url_for("index"))


@app.route("/exportar-sheets", methods=["POST"])
def exportar_sheets():
    """Exportar controles para Google Sheets"""
    try:
        # Verificar se o arquivo de credenciais existe
        credentials_path = "credentials.json"
        if not os.path.exists(credentials_path):
            flash(
                "Arquivo de credenciais do Google não encontrado. Configure credentials.json primeiro.",
                "error",
            )
            return redirect(url_for("index"))

        # Configurar credenciais do Google Sheets
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_path, scope
        )
        client = gspread.authorize(creds)

        # Nome da planilha (você pode personalizar)
        sheet_name = request.form.get(
            "sheet_name", "Controle de Pressão Arterial")

        # Tentar abrir planilha existente ou criar nova
        try:
            spreadsheet = client.open(sheet_name)
            worksheet = spreadsheet.sheet1
            # Limpar dados existentes
            worksheet.clear()
        except gspread.SpreadsheetNotFound:
            spreadsheet = client.create(sheet_name)
            worksheet = spreadsheet.sheet1

        # Buscar todas as medições
        controles = Controle.query.order_by(
            Controle.data.desc(), Controle.hora.desc()).all()

        # Preparar dados para exportação
        headers = ["ID", "Data", "Hora", "Sistólica",
                   "Diastólica", "Frequência", "Observações"]
        data = [headers]

        for controle in controles:
            row = [
                controle.id,
                controle.data.strftime("%d/%m/%Y"),
                controle.hora.strftime("%H:%M"),
                controle.sistolica,
                controle.diastolica,
                controle.frequencia if controle.frequencia else "",
                controle.observacoes or "",
            ]
            data.append(row)

        # Atualizar planilha
        worksheet.update("A1", data)

        # Formatar cabeçalho
        worksheet.format(
            "A1:G1",
            {
                "textFormat": {"bold": True},
                "backgroundColor": {"red": 0.2, "green": 0.6, "blue": 0.9},
            },
        )

        flash(
            f'Medições exportadas com sucesso para "{sheet_name}"!', "success")

    except Exception as e:
        flash(f"Erro ao exportar para Google Sheets: {str(e)}", "error")

    return redirect(url_for("index"))


@app.route("/teste")
def api_teste():
    return "{'teste': 'Ok'}"


@app.route("/api/controles")
def api_controles():
    """API para obter controles em formato JSON"""
    controles = Controle.query.order_by(
        Controle.data.desc(), Controle.hora.desc()).all()
    return jsonify([controle.to_dict() for controle in controles])


@app.route("/health", methods=["GET"])
def health_check():
    try:
        # Testa conexão com o banco
        db.session.execute(text("SELECT 1"))
        db_ok = True
    except Exception as e:
        db_ok = False

    status_code = 200 if db_ok else 500

    return jsonify({
        "status": "ok" if db_ok else "error",
        "database": "ok" if db_ok else "error",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }), status_code


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 12080))
    app.run(debug=True, host="0.0.0.0", port=port)
