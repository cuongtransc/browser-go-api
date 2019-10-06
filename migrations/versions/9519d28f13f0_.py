"""empty message

Revision ID: 9519d28f13f0
Revises: 
Create Date: 2019-10-02 13:54:17.877590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9519d28f13f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_rooms',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.Column('language', sa.Enum(name='languages'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('time_settings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('main_time', sa.Enum('BYOYOMI', 'ABSOLUTE', 'HOURGLASS', 'NONE', name='timetypes'), nullable=False),
    sa.Column('time_period', sa.Integer(), nullable=True),
    sa.Column('period_length', sa.Integer(), nullable=True),
    sa.Column('overtime', sa.Enum('BYOYOMI', 'ABSOLUTE', 'HOURGLASS', 'NONE', name='timetypes'), nullable=False),
    sa.Column('overtime_period', sa.Integer(), nullable=True),
    sa.Column('overtime_length', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.Integer(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('rank', sa.Enum('D7', 'D6', 'D5', 'D4', 'D3', 'D2', 'D1', 'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20', 'K21', 'K22', 'K23', 'K24', 'K25', 'K26', 'K27', 'K28', 'K29', 'K30', name='ranks'), nullable=True),
    sa.Column('elo', sa.Integer(), nullable=True),
    sa.Column('rank_certainty', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('komi', sa.Numeric(precision=2, scale=1), nullable=False),
    sa.Column('handicap', sa.Integer(), nullable=False),
    sa.Column('board_size', sa.Integer(), nullable=False),
    sa.Column('win_type', sa.Enum('DRAW', 'RESIGN', 'SCORE', 'TIME', 'VOID', name='wintype'), nullable=True),
    sa.Column('winner', sa.Enum('BLACK', 'WHITE', 'VOID', name='players'), nullable=True),
    sa.Column('score', sa.Numeric(precision=2, scale=1), nullable=True),
    sa.Column('white_captures', sa.Integer(), nullable=True),
    sa.Column('black_captures', sa.Integer(), nullable=True),
    sa.Column('application', sa.String(length=40), nullable=True),
    sa.Column('application_version', sa.String(length=20), nullable=True),
    sa.Column('event', sa.String(length=40), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('round', sa.Integer(), nullable=True),
    sa.Column('game_room', sa.Integer(), nullable=True),
    sa.Column('time_settings', sa.Integer(), nullable=True),
    sa.Column('player_black', sa.Integer(), nullable=True),
    sa.Column('player_white', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_room'], ['game_rooms.id'], ),
    sa.ForeignKeyConstraint(['player_black'], ['users.id'], ),
    sa.ForeignKeyConstraint(['player_white'], ['users.id'], ),
    sa.ForeignKeyConstraint(['time_settings'], ['time_settings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moves',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('player', sa.Enum('BLACK', 'WHITE', name='players'), nullable=True),
    sa.Column('x_point', sa.Integer(), nullable=True),
    sa.Column('y_point', sa.Integer(), nullable=True),
    sa.Column('move_number', sa.Integer(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=False),
    sa.Column('preceding_move', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game'], ['games.id'], ),
    sa.ForeignKeyConstraint(['preceding_move'], ['moves.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('move', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['move'], ['moves.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    op.drop_table('moves')
    op.drop_table('games')
    op.drop_table('users')
    op.drop_table('time_settings')
    op.drop_table('game_rooms')
    # ### end Alembic commands ###
