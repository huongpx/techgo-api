"""add image table

Revision ID: e7837c59f426
Revises: f110a7a08610
Create Date: 2023-03-09 11:41:28.733552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7837c59f426'
down_revision = 'f110a7a08610'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_variant_image',
    sa.Column('product_variant_id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('discount', sa.Column('product_variant_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'discount', 'product_variant', ['product_variant_id'], ['id'])
    op.drop_constraint('product_variant_discount_id_fkey', 'product_variant', type_='foreignkey')
    op.drop_column('product_variant', 'discount_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_variant', sa.Column('discount_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('product_variant_discount_id_fkey', 'product_variant', 'discount', ['discount_id'], ['id'])
    op.drop_constraint(None, 'discount', type_='foreignkey')
    op.drop_column('discount', 'product_variant_id')
    op.drop_table('product_variant_image')
    # ### end Alembic commands ###
