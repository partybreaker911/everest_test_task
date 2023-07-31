"""empty message

Revision ID: 9db68ef39563
Revises: 4ff5c8b035db
Create Date: 2023-07-29 20:54:00.845030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9db68ef39563'
down_revision = '4ff5c8b035db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'customer', ['customer_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('customer_id')

    # ### end Alembic commands ###
