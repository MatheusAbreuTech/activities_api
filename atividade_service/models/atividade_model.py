from config import db
from dataclasses import dataclass
from .resposta_model import Resposta

@dataclass
class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String, nullable=False)
    id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)

    respostas = db.relationship('Resposta', back_populates='atividade', cascade='all, delete-orphan')

    def __init__(self, id_disciplina, enunciado):
        self.id_disciplina = id_disciplina
        self.enunciado = enunciado

    def __repr__(self):
        return f"Atividade(id={self.id}, id_disciplina={self.id_disciplina}, enunciado={self.enunciado})"

    def to_dict(self):
        return {
            'id': self.id,
            'id_disciplina': self.id_disciplina,
            'enunciado': self.enunciado,
        }
