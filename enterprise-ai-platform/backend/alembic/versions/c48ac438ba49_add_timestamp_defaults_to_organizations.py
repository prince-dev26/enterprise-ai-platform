"""add timestamp defaults to organizations

Revision ID: c48ac438ba49
Revises: 7fbf4c260326
Create Date: 2026-08-20 13:40:29.624813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c48ac438ba49'
down_revision: Union[str, Sequence[str], None] = '7fbf4c260326'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# from alembic import op
# import sqlalchemy as sa


def upgrade():
    op.alter_column(
        "organizations",
        "created_at",
        server_default=sa.text("CURRENT_TIMESTAMP"),
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
    )

    op.alter_column(
        "organizations",
        "updated_at",
        server_default=sa.text("CURRENT_TIMESTAMP"),
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
    )


def downgrade():
    op.alter_column(
        "organizations",
        "updated_at",
        server_default=None,
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
    )

    op.alter_column(
        "organizations",
        "created_at",
        server_default=None,
        existing_type=sa.DateTime(timezone=True),
        existing_nullable=False,
    )