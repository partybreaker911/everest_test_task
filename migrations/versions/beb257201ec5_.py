"""empty message

Revision ID: beb257201ec5
Revises: 
Create Date: 2023-07-28 02:06:58.294133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beb257201ec5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('color', sa.String(length=80), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('delivery_status', sa.Enum('PENDING', 'DELIVERED', 'CANCELLED', name='deliverystatus'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('products')
    # ### end Alembic commands ###