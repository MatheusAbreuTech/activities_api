from config import create_app
from controllers.atividade_controller import atividade_bp
from controllers.disciplina_controller import disciplina_bp
from controllers.resposta_controller import resposta_bp

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')
app.register_blueprint(disciplina_bp, url_prefix='/disciplinas')
app.register_blueprint(resposta_bp, url_prefix='/respostas')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)