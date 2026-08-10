from uuid import UUID

from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    slug: str


class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    slug: str
    is_active: bool