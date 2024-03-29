"""nevers

Revision ID: 1197094762ef
Revises: 84e199f9cb91
Create Date: 2023-06-20 13:47:07.637542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1197094762ef'
down_revision = '84e199f9cb91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_category', sa.String(), nullable=False),
    sa.Column('be_something', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_category')
    )
    op.add_column('events', sa.Column('type_category', sa.String(), nullable=True))
    op.create_foreign_key(None, 'events', 'categories', ['type_category'], ['event_category'])
    op.drop_column('events', 'type_')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('type_', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'type_category')
    op.drop_table('categories')
    # ### end Alembic commands ###
