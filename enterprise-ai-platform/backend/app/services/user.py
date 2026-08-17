from app.models.user import User
from app.repositories.organization import OrganizationRepository
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.security.password import hash_password
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        self.organization_repository = OrganizationRepository(db)

    def create(self, data: UserCreate) -> User:
        organization = self.organization_repository.get_by_id(
            data.organization_id
        )

        if organization is None:
            raise ValueError("Organization not found")

        existing_user = self.user_repository.get_by_email(
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

        return self.user_repository.create(user)