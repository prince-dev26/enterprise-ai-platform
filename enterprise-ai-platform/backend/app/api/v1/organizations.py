from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.organization import OrganizationCreate, OrganizationRead
from app.services.organization import OrganizationService
from uuid import UUID


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "",
    response_model=OrganizationRead,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    data: OrganizationCreate,
    db: Session = Depends(get_db),
) -> OrganizationRead:
    service = OrganizationService(db)

    try:
        organization = service.create(data)
        db.commit()
        db.refresh(organization)

        return organization

    except ValueError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


@router.get(
    "/{organization_id}",
    response_model=OrganizationRead,
  )
def get_organization(
    organization_id: UUID,
    db: Session = Depends(get_db),
) -> OrganizationRead:
     service = OrganizationService(db)

     organization = service.get_by_id(organization_id)
     if organization is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )
     return organization

@router.get(
    "",
    response_model=list[OrganizationRead],
)
def get_organizations(
    db: Session = Depends(get_db),
) -> list[OrganizationRead]:
    service = OrganizationService(db)

    return service.get_all()