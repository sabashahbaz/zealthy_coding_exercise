"""empty message

Revision ID: 0436eb56e5da
Revises: 5a131c4cbb1a
Create Date: 2023-11-28 15:17:32.565871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0436eb56e5da'
down_revision = '5a131c4cbb1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_form_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_response', sa.String(length=1000), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_form_table', schema=None) as batch_op:
        batch_op.drop_column('admin_response')

    # ### end Alembic commands ###
