from config import db
from dataclasses import dataclass

@dataclass
class Disciplina(db.Model):
    __tablename__ = 'disciplina'
      
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    publica = db.Column(db.Boolean, default=False, nullable=False)
    
    def __init__(self, nome, publica=False):
        self.nome = nome
        self.publica = publica
        
    def __repr__(self):
        return f"<Disciplina id={self.id}, nome={self.nome}, publica={self.publica}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'publica': self.publica
        }