"""Add public tag to project

Revision ID: f3a10c95079f
Revises: 9d5ff5377b63
Create Date: 2025-01-14 22:01:12.694786

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f3a10c95079f"
down_revision = "54d9cae546ad"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "projects", sa.Column("public", sa.Boolean(), server_default=sa.sql.False_())
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("projects", "public")
    # ### end Alembic commands ###
