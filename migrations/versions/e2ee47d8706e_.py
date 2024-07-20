"""empty message

Revision ID: e2ee47d8706e
Revises: 1b133d443dcb
Create Date: 2024-07-20 10:19:15.649986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2ee47d8706e'
down_revision = '1b133d443dcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_video', sa.String(length=120), nullable=False),
    sa.Column('category', sa.String(length=120), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('author', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('author'),
    sa.UniqueConstraint('category'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('title'),
    sa.UniqueConstraint('url_video')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.create_unique_constraint(None, ['role'])
        batch_op.create_unique_constraint(None, ['lastname'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('lastname')
        batch_op.drop_column('name')
        batch_op.drop_column('role')

    op.drop_table('lesson')
    # ### end Alembic commands ###
