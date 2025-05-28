from models.resposta_model import Resposta
from models.atividade_model import Atividade
from clients.aluno_service_client import AlunoServiceClient
from config import db

class AtividadeNotFound(Exception):
    pass

class RespostaNaoEncontrada(Exception):
    pass

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

def get_resposta(id_resposta):
    resposta = Resposta.query.get(id_resposta)
    if not resposta:
        raise RespostaNaoEncontrada(f'Resposta com id {id_resposta} nao encontrada.')
    return resposta.to_dict(), 200

def delete_resposta(id_resposta):
    resposta = Resposta.query.get(id_resposta)
    if not resposta:
        raise RespostaNaoEncontrada(f'Resposta com id {id_resposta} nao encontrada.')
    db.session.delete(resposta)
    db.session.commit()
    return {'message': 'Resposta deletada com sucesso'}, 200

def update_resposta(id_atividade, id_resposta, resposta, nota, id_aluno):
    get_resposta = Resposta.query.get(id_resposta)
    if not resposta:
        raise RespostaNaoEncontrada(f'Resposta com id {id_resposta} nao encontrada.')
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(f'Atividade com id {id_atividade} não encontrada.')
    
    aluno_existe = AlunoServiceClient.verificar_aluno_existe(id_aluno)
    if not aluno_existe:
        return {'erro': 'Aluno nao encontrado'}, 404
    
    get_resposta.resposta = resposta
    get_resposta.nota = nota
    get_resposta.id_atividade = id_atividade
    get_resposta.id_aluno = id_aluno
    db.session.commit()
    return {'message': 'Resposta atualizada com sucesso', 'resposta': get_resposta.to_dict()}, 200