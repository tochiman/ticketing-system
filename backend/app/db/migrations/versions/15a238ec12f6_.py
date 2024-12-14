"""empty message

Revision ID: 15a238ec12f6
Revises: e1ddef123e7f
Create Date: 2024-12-10 07:03:12.230191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15a238ec12f6'
down_revision: Union[str, None] = 'e1ddef123e7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
