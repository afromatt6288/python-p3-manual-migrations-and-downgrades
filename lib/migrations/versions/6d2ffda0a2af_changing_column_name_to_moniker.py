"""changing column name to moniker

Revision ID: 6d2ffda0a2af
Revises: 791279dd0760
Create Date: 2023-03-22 16:56:20.340616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d2ffda0a2af'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='moniker')
    pass


def downgrade() -> None:
    op.alter_column('students', 'moniker', new_column_name='name')
    pass
