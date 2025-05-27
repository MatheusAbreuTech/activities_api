from config import db
from dataclasses import dataclass

@dataclass
class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.String, nullable=False)
    nota = db.Column(db.Float, nullable=True)

    id_atividade = db.Column(db.Integer, db.ForeignKey('atividade.id'), nullable=False)
    atividade = db.relationship('Atividade', back_populates='respostas')

    def __init__(self, id_aluno, id_atividade, resposta, nota=None):
        self.id_aluno = id_aluno
        self.id_atividade = id_atividade
        self.resposta = resposta
        self.nota = nota

    def __repr__(self):
        return f"Resposta(id={self.id}, id_aluno={self.id_aluno}, id_atividade={self.id_atividade}, resposta={self.resposta}, nota={self.nota})"

    def to_dict(self):
        return {
            'id': self.id,
            'id_aluno': self.id_aluno,
            'id_atividade': self.id_atividade,
            'resposta': self.resposta,
            'nota': self.nota
        }