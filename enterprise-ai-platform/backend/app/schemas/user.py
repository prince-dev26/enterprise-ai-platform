from datetime import datetime
from uuid import UUID


from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    organization_id: UUID
    email: EmailStr
    password: str
    first_name: str
    last_name: str

class UserResponse(BaseModel):
    id: UUID
    organization_id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool | None = None

class UserRead(BaseModel):
    id: UUID
    organization_id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
    }