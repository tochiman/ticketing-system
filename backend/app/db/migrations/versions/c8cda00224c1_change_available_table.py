"""change available table

Revision ID: c8cda00224c1
Revises: f8533cedf560
Create Date: 2024-12-17 15:57:40.407776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision: str = 'c8cda00224c1'
down_revision: Union[str, None] = 'f8533cedf560'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('available', sa.Column('available_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('available', 'available_id')
    # ### end Alembic commands ###