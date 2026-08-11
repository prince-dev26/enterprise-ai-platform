from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.security.password import hash_password


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create(self, data: UserCreate) -> User:
        existing_user = self.repository.get_by_email(
            email=data.email,
            organization_id=data.organization_id,
        )

        if existing_user:
            raise ValueError("User email already exists")

        user = User(
            organization_id=data.organization_id,
            email=data.email,
            password_hash=hash_password(data.password),
            first_name=data.first_name,
            last_name=data.last_name,
        )

        return self.repository.create(user)