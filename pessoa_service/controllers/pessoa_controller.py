from flask import Blueprint, jsonify
from services import pessoa_service_client

pessoa_bp = Blueprint('pessoa_bp', __name__)

@pessoa_bp.route('/professores', methods=['GET'])
def listar_professores():
    professores = pessoa_service_client.listar_professores()
    return jsonify(professores)

@pessoa_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = pessoa_service_client.listar_alunos()
    return jsonify(alunos)

@pessoa_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>', methods=['GET'])
def verificar_leciona(id_professor, id_disciplina):
    try:
        leciona = pessoa_service_client.leciona(id_professor, id_disciplina)
        return jsonify({'leciona': leciona})
    except pessoa_service_client.DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404
