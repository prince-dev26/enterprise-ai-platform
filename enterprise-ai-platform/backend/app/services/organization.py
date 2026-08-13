from uuid import UUID

from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.repositories.organization import OrganizationRepository
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


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

    def update(
        self,
        organization_id: UUID,
        data: OrganizationUpdate,
    ) -> Organization | None:

        organization = self.repository.get_by_id(organization_id)

        if organization is None:
            return None

        update_data = data.model_dump(exclude_unset=True)

        if "slug" in update_data:
            existing_organization = self.repository.get_by_slug(
                update_data["slug"]
            )

            if (
                existing_organization
                and existing_organization.id != organization_id
            ):
                raise ValueError("Organization slug already exists")

        return self.repository.update(
            organization=organization,
            data=update_data,
        )

    def get_by_id(
        self,
        organization_id: UUID,
    ) -> Organization | None:
        return self.repository.get_by_id(organization_id)

    def get_all(
        self,
        page: int,
        page_size: int,
    ) -> list[Organization]:
        return self.repository.get_all(
            page=page,
            page_size=page_size,
        )

    def deactivate(
     self,
     organization_id: UUID,
    ) -> Organization | None:
     organization = self.repository.get_by_id(organization_id)

     if organization is None:
        return None

     return self.repository.deactivate(organization)