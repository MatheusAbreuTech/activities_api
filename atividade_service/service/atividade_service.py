from models.atividade_model import Atividade

from models.resposta_model import Resposta
from clients.aluno_service_client import AlunoServiceClient
from service.disciplina_service import obter_disciplina
from config import db

class AtividadeNotFound(Exception):
    pass

class RespostaNaoEncontrada(Exception):
    pass

def listar_atividades():
    atividades = Atividade.query.all()
    return [
        {
            **atividade.to_dict(),
            'respostas': [resposta.to_dict() for resposta in atividade.respostas]
        }
        for atividade in atividades
    ]

def obter_atividade(id_atividade):
    if(id_atividade is None):
        return {'erro': 'Id da atividade é obrigatorio'}, 400
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} não encontrada.')
    return {**atividade.to_dict(), 'respostas': [resposta.to_dict() for resposta in atividade.respostas]}, 200

def cadastrar_atividade(id_disciplina, enunciado):
    if(enunciado is None):  
        return {'erro': 'Enunciado é obrigatorio'}, 400
    if(id_disciplina is None):
        return {'erro': 'Disciplina é obrigatorio'}, 400
    
    obter_disciplina(id_disciplina)
    
    atividade = Atividade(id_disciplina=id_disciplina, enunciado=enunciado)
    
    db.session.add(atividade)
    db.session.commit()
    db.session.refresh(atividade)
    
    return atividade.to_dict(), 201

def delete_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} nao encontrada.')
    db.session.delete(atividade)
    db.session.commit()
    return {'message': 'Atividade deletada com sucesso'}, 200

def update_atividade(id_atividade, enunciado):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} nao encontrada.')
    atividade.enunciado = enunciado
    db.session.commit()
    return {'message': 'Atividade atualizada com sucesso', 'atividade': atividade.to_dict()}, 200
