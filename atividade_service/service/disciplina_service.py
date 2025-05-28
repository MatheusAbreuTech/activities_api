from models.disciplina_model import Disciplina
from config import db

class DisciplinaNaoEncontrada(Exception):
    pass

def obter_disciplina(id_disciplina):
    disciplina = Disciplina.query.get(id_disciplina)
    if not disciplina:
        raise DisciplinaNaoEncontrada(f'Disciplina com id {id_disciplina} não encontrada.')
    return disciplina.to_dict(), 200

def obter_disciplinas():
    disciplinas = Disciplina.query.all()
    return [disciplina.to_dict() for disciplina in disciplinas], 200

def cadastrar_disciplina(nome, publica=False):
    if (nome is None):
        return {'erro': 'Nome é obrigatorio'}, 400
    
    disciplina = Disciplina(nome=nome, publica=publica)
    
    db.session.add(disciplina)
    db.session.commit()
    db.session.refresh(disciplina)
    return disciplina.to_dict(), 201

def update_disciplina(id_disciplina, nome, publica):
    disciplina = Disciplina.query.get(id_disciplina)
    if not disciplina:
        raise DisciplinaNaoEncontrada(f'Disciplina com id {id_disciplina} nao encontrada.')
    disciplina.nome = nome
    disciplina.publica = publica
    db.session.commit()
    return {
        'message': 'Disciplina atualizada com sucesso', 
        'disciplina': disciplina.to_dict()
        }, 200

def delete_disciplina(id_disciplina):
    disciplina = Disciplina.query.get(id_disciplina)
    if not disciplina:
        raise DisciplinaNaoEncontrada(f'Disciplina com id {id_disciplina} nao encontrada.')
    db.session.delete(disciplina)
    db.session.commit()
    return {'message': 'Disciplina deletada com sucesso'}, 200
