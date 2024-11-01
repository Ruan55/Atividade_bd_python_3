from models.user import Aluno
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save_user(self, user: Aluno):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

    def search_user_by_email(self, email: str):
        return self.session.query(Aluno).filter_by(email=email).first()
    
    def delete_user(self, user: Aluno):
        self.session.delete(user)
        self.session.commit()
        self.session.refresh(user)

    def list_all_users(self):
        return self.session.query(Aluno).all()