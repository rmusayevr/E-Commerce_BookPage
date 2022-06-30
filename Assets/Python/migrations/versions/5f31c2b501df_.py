"""empty message

Revision ID: 5f31c2b501df
Revises: 47db1020a569
Create Date: 2022-05-06 22:28:22.547300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f31c2b501df'
down_revision = '47db1020a569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lang_code', sa.String(length=10), nullable=False),
    sa.Column('lang_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=16, asdecimal=2), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.ForeignKeyConstraint(['language_id'], ['Language.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Book')
    op.drop_table('Language')
    op.drop_table('Genre')
    # ### end Alembic commands ###
