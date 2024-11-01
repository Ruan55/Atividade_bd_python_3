from models.user import Aluno
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self,ra: int, name: str, last_name: str,  email: str, password: str):
        try:
            aluno = Aluno(ra=ra, name=name, last_name=last_name, email=email, password=password)
            cadastro = self.repository.search_user_by_email(email=aluno.email)

            if cadastro:
                print("Usuário já cadastrado!")
                return

            self.repository.save_user(user=aluno)
            print("Usuário cadastrado com sucesso!")
        except TypeError as error:
            print(f"Erro ao salvar o arquivo: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")
    
    def list_all_users(self):
        return self.repository.list_all_users()