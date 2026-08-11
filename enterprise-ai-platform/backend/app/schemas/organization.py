from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict


class OrganizationCreate(BaseModel):
    name: str
    slug: str


class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    slug: str
    is_active: bool


class OrganizationRead(BaseModel):
    id: UUID
    name: str
    slug: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
    }

class OrganizationUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    is_active: bool | None = None