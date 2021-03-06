"""posts table

Revision ID: 86dde823bcc9
Revises: b50bcc1b3b21
Create Date: 2018-08-06 00:43:21.384012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86dde823bcc9'
down_revision = 'b50bcc1b3b21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
