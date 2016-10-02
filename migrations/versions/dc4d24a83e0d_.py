"""empty message

Revision ID: dc4d24a83e0d
Revises: ddf1e4277864
Create Date: 2016-09-27 22:44:56.560000

"""

# revision identifiers, used by Alembic.
revision = 'dc4d24a83e0d'
down_revision = 'ddf1e4277864'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('zhulong_shared_images', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('zhulong_shared_images', 'is_locked',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('zhulong_shared_images', 'is_shared',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('zhulong_system_images', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('zhulong_user', 'blocked',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('zhulong_user', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               type_=mysql.BIGINT(display_width=20, unsigned=True))
    op.alter_column('zhulong_user', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=False)
    op.alter_column('zhulong_user_containers', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('zhulong_user_containers', 'is_running',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('zhulong_user_containers', 'is_running',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('zhulong_user_containers', 'is_deleted',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('zhulong_user', 'is_active',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('zhulong_user', 'id',
               existing_type=mysql.BIGINT(display_width=20, unsigned=True),
               type_=mysql.INTEGER(display_width=11))
    op.alter_column('zhulong_user', 'blocked',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('zhulong_system_images', 'is_deleted',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('zhulong_shared_images', 'is_shared',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('zhulong_shared_images', 'is_locked',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('zhulong_shared_images', 'is_deleted',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    ### end Alembic commands ###