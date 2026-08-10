from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.organization import Organization


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    organization_id: Mapped[UUID] = mapped_column(
    UUID(as_uuid=True),
    ForeignKey("organizations.id", ondelete="CASCADE"),
    nullable=False,
    index=True,
    )
    organization: Mapped["Organization"] = relationship(
    back_populates="users",
    )

    email: Mapped[str] = mapped_column(
    String(320),
    nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
    String(255),
    nullable=False,
    )

    first_name: Mapped[str] = mapped_column(
    String(100),
    nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
    String(100),
    nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
    Boolean,
    nullable=False,
    default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    default=lambda: datetime.now(timezone.utc),
    onupdate=lambda: datetime.now(timezone.utc),
    )