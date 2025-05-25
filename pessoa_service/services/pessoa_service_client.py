import requests

class DisciplinaNaoEncontrada(Exception):
    pass

def listar_professores():
    try:
        r = requests.get("http://localhost:5001/pessoas/professores")
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        return f"Erro ao listar professores: {e}"

def listar_alunos():
    try:
        r = requests.get("http://localhost:5001/pessoas/alunos")
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        return f"Erro ao listar alunos: {e}"

def leciona(id_professor, id_disciplina):
    GERENCIADOR_ESCOLAR = "http://localhost:5000/professor/"
    """Verifica se um professor leciona uma disciplina específica."""
    url = f"{GERENCIADOR_ESCOLAR}/{id_professor}/{id_disciplina}"
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            return id_professor in disciplina['professores']
    raise DisciplinaNaoEncontrada




class PessoaServiceClient:
    @staticmethod
    def verificar_leciona(id_professor, id_disciplina):
        url = f"{PESSOA_SERVICE_URL}/leciona/{id_professor}/{id_disciplina}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('leciona', False) if data.get('isok') else False
        except requests.RequestException as e:
            print(f"Erro ao acessar o pessoa_service: {e}")
            return False