"""06.09.2023-15:15:53

Revision ID: 26fc651d0e89
Revises: 67b265e62fd6
Create Date: 2023-09-06 15:16:01.064670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26fc651d0e89'
down_revision: Union[str, None] = '67b265e62fd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('cloud_public_id', sa.String(length=128), nullable=False))
    op.add_column('images', sa.Column('cloud_version', sa.String(length=128), nullable=False))
    op.create_unique_constraint(None, 'images', ['cloud_public_id'])
    op.create_unique_constraint(None, 'images', ['cloud_version'])
    op.drop_column('images', 'asset_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('asset_id', sa.VARCHAR(length=32), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'images', type_='unique')
    op.drop_constraint(None, 'images', type_='unique')
    op.drop_column('images', 'cloud_version')
    op.drop_column('images', 'cloud_public_id')
    # ### end Alembic commands ###
