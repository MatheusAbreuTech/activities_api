from flask import Blueprint, jsonify, request
from service.disciplina_service import DisciplinaNaoEncontrada, obter_disciplina, cadastrar_disciplina, delete_disciplina, update_disciplina, obter_disciplinas

disciplina_bp = Blueprint('disciplina_bp', __name__)

@disciplina_bp.route('/<int:id_disciplina>', methods=['GET'])
def obter_disciplina_route(id_disciplina):
    try:
        disciplina, code = obter_disciplina(id_disciplina)
        return jsonify(disciplina), code
    except DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404

@disciplina_bp.route('/', methods=['POST'])
def cadastrar_disciplina_route():
    data = request.get_json()
    nome = data.get('nome', None)
    publica = data.get('publica', False)
    
    disciplina, code = cadastrar_disciplina(nome=nome, publica=publica)
    return jsonify(disciplina), code

@disciplina_bp.route('/<int:id_disciplina>', methods=['DELETE'])
def delete_disciplina_route(id_disciplina):
    try:
        disciplina, code = delete_disciplina(id_disciplina=id_disciplina)
        return jsonify(disciplina), code
    except DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina nao encontrada'}), 404  
            
@disciplina_bp.route('/<int:id_disciplina>', methods=['PUT'])
def update_disciplina_route(id_disciplina):
    try:
        data = request.get_json()
        id=data.get('id', None)
        nome=data.get('nome', None)
        publica=data.get('publica', None)
        disciplina, code = update_disciplina(id_disciplina=id_disciplina, nome=nome, publica=publica)
        return jsonify(disciplina), code
    except DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina nao encontrada'}), 404
    
@disciplina_bp.route('/', methods=['GET'])
def obter_disciplinas_route():
    atividade, code = obter_disciplinas()
    return jsonify(atividade), code