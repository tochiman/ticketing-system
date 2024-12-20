"""init


Revision ID: c4c35a60946c
Revises: 
Create Date: 2024-11-26 07:55:37.796395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision: str = 'c4c35a60946c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allergy',
    sa.Column('allergy_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('allergy_id')
    )
    op.create_table('customer',
    sa.Column('customer_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(max_length=1137), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('customer_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('organization',
    sa.Column('organization_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(max_length=1137), nullable=False),
    sa.PrimaryKeyConstraint('organization_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('session',
    sa.Column('session_id', sa.String(length=128), nullable=False),
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('user_type', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('item',
    sa.Column('item_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('organization_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('size', sa.String(length=256), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.organization_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('order',
    sa.Column('order_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('customer_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('point_history',
    sa.Column('point_history_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('customer_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('charge', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ),
    sa.PrimaryKeyConstraint('point_history_id')
    )
    op.create_table('store',
    sa.Column('store_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('organization_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(max_length=1137), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=False),
    sa.Column('latitude', sa.String(length=11), nullable=False),
    sa.Column('longitude', sa.String(length=11), nullable=False),
    sa.Column('open_time', sa.Time(), nullable=False),
    sa.Column('close_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.organization_id'], ),
    sa.PrimaryKeyConstraint('store_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('available',
    sa.Column('store_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('item_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.item_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.store_id'], ),
    sa.PrimaryKeyConstraint('store_id', 'item_id')
    )
    op.create_table('item_to_allergy',
    sa.Column('item_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('allergy_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['allergy_id'], ['allergy.allergy_id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.item_id'], ),
    sa.PrimaryKeyConstraint('item_id', 'allergy_id')
    )
    op.create_table('order_detail',
    sa.Column('order_detail_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('order_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('item_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('number_of_purchase', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.item_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('order_detail_id')
    )
    op.create_table('payment',
    sa.Column('payment_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('order_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False)            , default=uuid.uuid4, nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('payment_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('order_detail')
    op.drop_table('item_to_allergy')
    op.drop_table('available')
    op.drop_table('store')
    op.drop_table('point_history')
    op.drop_table('order')
    op.drop_table('item')
    op.drop_table('session')
    op.drop_table('organization')
    op.drop_table('customer')
    op.drop_table('allergy')
    # ### end Alembic commands ###
