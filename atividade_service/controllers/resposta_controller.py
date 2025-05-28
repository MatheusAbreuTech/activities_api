from flask import Blueprint, jsonify, request
from service.resposta_service import AtividadeNotFound,RespostaNaoEncontrada, update_resposta, cadastrar_resposta, delete_resposta, get_resposta

resposta_bp = Blueprint('resposta_bp', __name__)

@resposta_bp.route('/<int:id_atividade>', methods=['POST'])
def cadastrar_resposta_route(id_atividade):
    try:
        data = request.get_json()
        resposta = data.get('resposta', None)
        id_aluno = data.get('id_aluno', None)
        nota = data.get('nota', None)
        
        resposta, code = cadastrar_resposta(id_atividade=id_atividade, id_aluno=id_aluno, resposta=resposta)
        return jsonify(resposta), code
    except RespostaNaoEncontrada:
        return jsonify({'erro': 'Resposta não encontrada'}), 404
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    
@resposta_bp.route('/<int:id_resposta>', methods=['GET'])
def obter_resposta_route(id_resposta):
    try:
        resposta, code = get_resposta(id_resposta=id_resposta)
        return jsonify(resposta), code
    except RespostaNaoEncontrada:
        return jsonify({'erro': 'Resposta não encontrada'}), 404    
    
@resposta_bp.route('/atividade/<int:id_atividade>/resposta/<int:id_resposta>', methods=['PUT'])
def update_resposta_route(id_atividade, id_resposta):
    try:
        data = request.get_json()
        resposta = data.get('resposta', None)
        id_aluno = data.get('id_aluno', None)
        nota = data.get('nota', None)
        resposta, code = update_resposta(id_atividade, id_resposta, resposta, nota, id_aluno)
        return jsonify(resposta), code
    except RespostaNaoEncontrada:
        return jsonify({'erro': 'Resposta não encontrada'}), 404
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    
@resposta_bp.route('/<int:id_resposta>', methods=['DELETE'])    
def delete_resposta_route(id_resposta):
    try:
        resposta, code = delete_resposta(id_resposta)
        return jsonify(resposta), code
    except RespostaNaoEncontrada:
        return jsonify({'erro': 'Resposta não encontrada'}), 404