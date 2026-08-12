from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.organization import Organization


class OrganizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, organization_id: UUID) -> Organization | None:
        statement = select(Organization).where(Organization.id == organization_id)

        return self.db.scalar(statement)

    def get_by_slug(self, slug: str) -> Organization | None:
        statement = select(Organization).where(Organization.slug == slug)

        return self.db.scalar(statement)

    def create(self, organization: Organization) -> Organization:
        self.db.add(organization)
        self.db.flush()

        return organization

    def get_all(
        self,
        page: int,
        page_size: int,
    ) -> list[Organization]:
        offset = (page - 1) * page_size

        statement = (
            select(Organization)
            .order_by(Organization.created_at.desc())
            .offset(offset)
            .limit(page_size)
        )

        return list(self.db.scalars(statement).all())

    def update(
        self,
        organization: Organization,
        data: dict,
    ) -> Organization:
        for field, value in data.items():
            setattr(organization, field, value)

        self.db.flush()
        self.db.refresh(organization)

        return organization

    def deactivate(
     self,
     organization: Organization,
    ) -> Organization:
     organization.is_active = False

     self.db.flush()
     self.db.refresh(organization)

     return organization
