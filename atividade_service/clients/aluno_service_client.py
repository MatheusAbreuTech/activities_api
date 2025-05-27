import requests

ALUNO_SERVICE_URL = "http://web:5000/alunos"

class AlunoServiceClient:
    @staticmethod
    def verificar_aluno_existe(id_aluno):
        url = f"{ALUNO_SERVICE_URL}/{id_aluno}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return True if data.get('id') else False
        except requests.RequestException as e:
            print(f"Erro ao acessar o aluno_service: {e}")
            return False