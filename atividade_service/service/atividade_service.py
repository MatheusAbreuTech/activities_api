from models.atividade_model import Atividade
from models.disciplina_model import Disciplina
from models.resposta_model import Resposta
from clients.aluno_service_client import AlunoServiceClient
from config import db

class AtividadeNotFound(Exception):
    pass

class DisciplinaNaoEncontrada(Exception):
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

def obter_disciplina(id_disciplina):
    disciplina = Disciplina.query.get(id_disciplina)
    if not disciplina:
        raise DisciplinaNaoEncontrada(f'Disciplina com id {id_disciplina} não encontrada.')
    return disciplina.to_dict(), 200

def cadastrar_disciplina(nome, publica=False):
    if (nome is None):
        return {'erro': 'Nome é obrigatorio'}, 400
    
    disciplina = Disciplina(nome=nome, publica=publica)
    
    db.session.add(disciplina)
    db.session.commit()
    db.session.refresh(disciplina)
    return disciplina.to_dict(), 201

def cadastrar_resposta(id_atividade, id_aluno, resposta, nota=None):
    if(id_atividade is None):
        return {'erro': 'Id da atividade é obrigatorio'}, 400
    if(id_aluno is None):
        return {'erro': 'Id do aluno é obrigatorio'}, 400
    if(resposta is None):
        return {'erro': 'Resposta é obrigatorio'}, 400
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} não encontrada.')
    
    aluno_existe = AlunoServiceClient.verificar_aluno_existe(id_aluno)
    if not aluno_existe:
        return {'erro': 'Aluno nao encontrado'}, 404
    
    resposta = Resposta(id_aluno=id_aluno, id_atividade=id_atividade, resposta=resposta, nota=nota)
    db.session.add(resposta)
    db.session.commit()
    db.session.refresh(resposta)
    return resposta.to_dict(), 201


def delete_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} nao encontrada.'),400
    db.session.delete(atividade)
    db.session.commit()
    return {'message': 'Atividade deletada com sucesso'}, 200

def update_atividade(id_atividade, enunciado):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} nao encontrada.'),400
    atividade.enunciado = enunciado
    db.session.commit()
    return {'message': 'Atividade atualizada com sucesso'}, 200