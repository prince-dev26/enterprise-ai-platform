from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.repositories.organization import OrganizationRepository
from app.schemas.organization import OrganizationCreate


class OrganizationService:

    def __init__(self, db: Session):
        self.repository = OrganizationRepository(db)

    def create(self, data: OrganizationCreate) -> Organization:
        existing_organization = self.repository.get_by_slug(data.slug)

        if existing_organization:
            raise ValueError("Organization slug already exists")

        organization = Organization(
            name=data.name,
            slug=data.slug,
        )

        return self.repository.create(organization)