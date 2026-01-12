from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Controle(db.Model):
    """Modelo para armazenar controles de pressão arterial"""

    __tablename__ = "controles"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    hora = db.Column(db.Time, nullable=False, default=datetime.utcnow)
    sistolica = db.Column(db.Integer, nullable=False)
    diastolica = db.Column(db.Integer, nullable=False)
    frequencia = db.Column(db.Integer, nullable=True)
    observacoes = db.Column(db.Text, nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Controle {self.sistolica}/{self.diastolica} - {self.data}>"

    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            "id": self.id,
            "data": self.data.strftime("%d/%m/%Y"),
            "hora": self.hora.strftime("%H:%M:%S"),
            "sistolica": self.sistolica,
            "diastolica": self.diastolica,
            "frequencia": self.frequencia,
            "observacoes": self.observacoes,
            "criado_em": self.criado_em.strftime("%d/%m/%Y %H:%M:%S"),
        }
