from flask import Blueprint, jsonify, request
from service.atividade_service import AtividadeNotFound, cadastrar_atividade, listar_atividades, obter_atividade, delete_atividade, update_atividade
from service.disciplina_service import DisciplinaNaoEncontrada
from clients.pessoa_service_client import PessoaServiceClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['GET'])
def listar_atividades_route():
    atividades = listar_atividades()
    return jsonify(atividades)

@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade_route(id_atividade):
    try:
        atividade, code = obter_atividade(id_atividade)
        return jsonify(atividade), code
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    
@atividade_bp.route('/', methods=['POST'])
def cadastrar_atividade_route():
    try:
        data = request.get_json()
        id_disciplina = data.get('id_disciplina', None)
        enunciado = data.get('enunciado', None)
        atividade, code = cadastrar_atividade(id_disciplina, enunciado)
        return jsonify(atividade), code
    except DisciplinaNaoEncontrada as error:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404

@atividade_bp.route('/<int:id_atividade>', methods=['DELETE'])
def delete_atividade_route(id_atividade):
    try:
        atividade, code = delete_atividade(id_atividade=id_atividade)
        return jsonify(atividade), code
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade nao encontrada'}), 404

@atividade_bp.route('/<int:id_atividade>', methods=['PUT'])
def update_atividade_route(id_atividade):
    try:
        data = request.get_json()
        id=data.get('id', None)
        enunciado=data.get('enunciado', None)
        atividade, code = update_atividade(id_atividade=id_atividade, enunciado=enunciado)
        return jsonify(atividade), code
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade nao encontrada'}), 404    
                