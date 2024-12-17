"""Add disabled status

Revision ID: f8533cedf560
Revises: 772d37482e23
Create Date: 2024-12-15 21:43:29.601214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8533cedf560'
down_revision: Union[str, None] = '772d37482e23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('disabled', sa.Boolean(), nullable=False))
    op.drop_index('email', table_name='customer')
    op.add_column('organization', sa.Column('disabled', sa.Boolean(), nullable=False))
    op.drop_index('email', table_name='organization')
    op.add_column('reset_password', sa.Column('user_type', sa.Integer(), nullable=False))
    op.add_column('store', sa.Column('disabled', sa.Boolean(), nullable=False))
    op.drop_index('email', table_name='store')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('email', 'store', ['email'], unique=True)
    op.drop_column('store', 'disabled')
    op.drop_column('reset_password', 'user_type')
    op.create_index('email', 'organization', ['email'], unique=True)
    op.drop_column('organization', 'disabled')
    op.create_index('email', 'customer', ['email'], unique=True)
    op.drop_column('customer', 'disabled')
    # ### end Alembic commands ###