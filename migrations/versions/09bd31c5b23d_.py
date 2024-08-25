"""empty message

Revision ID: 09bd31c5b23d
Revises: 507e2222c27e
Create Date: 2023-12-30 19:53:06.727177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09bd31c5b23d'
down_revision = '507e2222c27e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uploaded_img_file', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('uploaded_img_file')

    # ### end Alembic commands ###