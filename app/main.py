from models.user import Aluno
from services.user_services import UserService
from repositories.user_repository import UserRepository
from config.connection import Session


def main():
    session = Session()
    repository = UserRepository(session)
    service = UserService(repository)

    for i in range(2):
        ra = input("Digite o seu ra: ")
        nome = input("Digite a seu nome: ")
        sobrenome = input("Digite o seu sobrenome: ")
        email = input("Digite a seu email: ")
        senha = input("Digite a sua senha: ")

        service.create_user(
            ra=ra, name=nome, last_name=sobrenome, email=email, password=senha
        )

    print("\nListando todos os usuários.")
    alunos = service.list_all_users()

    for aluno in alunos:
        print(f"{aluno.name} - {aluno.email}")


if __name__ == "__main__":
    main()
