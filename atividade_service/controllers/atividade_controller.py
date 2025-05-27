from flask import Blueprint, jsonify, request
from service.atividade_service import AtividadeNotFound, DisciplinaNaoEncontrada, cadastrar_resposta, cadastrar_atividade, listar_atividades, obter_atividade,cadastrar_disciplina, obter_disciplina
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

@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor_route(id_atividade, id_professor):
    try:
        atividade = obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except AtividadeNotFound(error):
        return jsonify(error), 404
    
@atividade_bp.route('/disciplina/<int:id_disciplina>', methods=['GET'])
def obter_disciplina_route(id_disciplina):
    try:
        disciplina, code = obter_disciplina(id_disciplina)
        return jsonify(disciplina), code
    except DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404

@atividade_bp.route('/disciplina', methods=['POST'])
def cadastrar_disciplina_route():
    data = request.get_json()
    nome = data.get('nome', None)
    publica = data.get('publica', False)
    
    disciplina, code = cadastrar_disciplina(nome=nome, publica=publica)
    return jsonify(disciplina), code

@atividade_bp.route('/resposta/<int:id_atividade>', methods=['POST'])
def cadastrar_resposta_route(id_atividade):
    try:
        data = request.get_json()
        resposta = data.get('resposta', None)
        id_aluno = data.get('id_aluno', None)
        nota = data.get('nota', None)
        
        resposta, code = cadastrar_resposta(id_atividade=id_atividade, id_aluno=id_aluno, resposta=resposta)
        return jsonify(resposta), code
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    