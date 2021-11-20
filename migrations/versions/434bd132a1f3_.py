"""empty message

Revision ID: 434bd132a1f3
Revises: 
Create Date: 2021-11-20 02:19:16.602370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '434bd132a1f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('empresa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('parada',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ubicacion', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ubicacion')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('linea',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_empresa', sa.Integer(), nullable=True),
    sa.Column('nombre_linea', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresa.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre_linea')
    )
    op.create_table('horario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_linea', sa.Integer(), nullable=True),
    sa.Column('id_parada', sa.Integer(), nullable=True),
    sa.Column('tipo_dia', sa.String(length=80), nullable=False),
    sa.Column('hora', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['id_linea'], ['linea.id'], ),
    sa.ForeignKeyConstraint(['id_parada'], ['parada.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reserva',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_linea', sa.Integer(), nullable=True),
    sa.Column('id_horario', sa.Integer(), nullable=True),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.Column('asiento', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['id_horario'], ['horario.id'], ),
    sa.ForeignKeyConstraint(['id_linea'], ['linea.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserva')
    op.drop_table('horario')
    op.drop_table('linea')
    op.drop_table('usuario')
    op.drop_table('parada')
    op.drop_table('empresa')
    op.drop_table('administrador')
    # ### end Alembic commands ###
