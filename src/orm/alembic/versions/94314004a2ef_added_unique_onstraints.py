"""Added unique onstraints

Revision ID: 94314004a2ef
Revises: 8777e0a9fc3f
Create Date: 2022-02-21 13:21:50.252704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94314004a2ef'
down_revision = '8777e0a9fc3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'condition', ['title'])
    op.create_unique_constraint(None, 'day_time', ['title'])
    op.create_unique_constraint(None, 'weather', ['date', 'day_time_id'])
    op.create_unique_constraint(None, 'weather_condition', ['weather_id', 'condition_id'])
    op.create_unique_constraint(None, 'wind_direction', ['direction'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wind_direction', type_='unique')
    op.drop_constraint(None, 'weather_condition', type_='unique')
    op.drop_constraint(None, 'weather', type_='unique')
    op.drop_constraint(None, 'day_time', type_='unique')
    op.drop_constraint(None, 'condition', type_='unique')
    # ### end Alembic commands ###