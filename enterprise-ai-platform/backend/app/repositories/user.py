from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(
        self,
        user_id: UUID,
        organization_id: UUID,
    ) -> User | None:
        statement = select(User).where(
            User.id == user_id,
            User.organization_id == organization_id,
        )

        return self.db.scalar(statement)

    def get_by_email(
        self,
        email: str,
        organization_id: UUID,
    ) -> User | None:
        statement = select(User).where(
            User.email == email,
            User.organization_id == organization_id,
        )

        return self.db.scalar(statement)

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.flush()

        return user