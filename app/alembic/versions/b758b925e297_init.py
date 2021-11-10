"""init

Revision ID: b758b925e297
Revises: 
Create Date: 2021-11-11 00:50:11.376445

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'b758b925e297'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conference',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_conference_description'), 'conference', ['description'], unique=False)
    op.create_index(op.f('ix_conference_end_date'), 'conference', ['end_date'], unique=False)
    op.create_index(op.f('ix_conference_id'), 'conference', ['id'], unique=False)
    op.create_index(op.f('ix_conference_start_date'), 'conference', ['start_date'], unique=False)
    op.create_index(op.f('ix_conference_title'), 'conference', ['title'], unique=False)
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('user_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('mail', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_person_id'), 'person', ['id'], unique=False)
    op.create_index(op.f('ix_person_mail'), 'person', ['mail'], unique=False)
    op.create_index(op.f('ix_person_user_name'), 'person', ['user_name'], unique=False)
    op.create_table('talk',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('duration', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('conference_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conference_id'], ['conference.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_talk_conference_id'), 'talk', ['conference_id'], unique=False)
    op.create_index(op.f('ix_talk_date_time'), 'talk', ['date_time'], unique=False)
    op.create_index(op.f('ix_talk_description'), 'talk', ['description'], unique=False)
    op.create_index(op.f('ix_talk_duration'), 'talk', ['duration'], unique=False)
    op.create_index(op.f('ix_talk_id'), 'talk', ['id'], unique=False)
    op.create_index(op.f('ix_talk_title'), 'talk', ['title'], unique=False)
    op.create_table('participanttalklink',
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('talk_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['talk_id'], ['talk.id'], ),
    sa.PrimaryKeyConstraint('person_id', 'talk_id')
    )
    op.create_index(op.f('ix_participanttalklink_person_id'), 'participanttalklink', ['person_id'], unique=False)
    op.create_index(op.f('ix_participanttalklink_talk_id'), 'participanttalklink', ['talk_id'], unique=False)
    op.create_table('speakertalklink',
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('talk_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['talk_id'], ['talk.id'], ),
    sa.PrimaryKeyConstraint('person_id', 'talk_id')
    )
    op.create_index(op.f('ix_speakertalklink_person_id'), 'speakertalklink', ['person_id'], unique=False)
    op.create_index(op.f('ix_speakertalklink_talk_id'), 'speakertalklink', ['talk_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_speakertalklink_talk_id'), table_name='speakertalklink')
    op.drop_index(op.f('ix_speakertalklink_person_id'), table_name='speakertalklink')
    op.drop_table('speakertalklink')
    op.drop_index(op.f('ix_participanttalklink_talk_id'), table_name='participanttalklink')
    op.drop_index(op.f('ix_participanttalklink_person_id'), table_name='participanttalklink')
    op.drop_table('participanttalklink')
    op.drop_index(op.f('ix_talk_title'), table_name='talk')
    op.drop_index(op.f('ix_talk_id'), table_name='talk')
    op.drop_index(op.f('ix_talk_duration'), table_name='talk')
    op.drop_index(op.f('ix_talk_description'), table_name='talk')
    op.drop_index(op.f('ix_talk_date_time'), table_name='talk')
    op.drop_index(op.f('ix_talk_conference_id'), table_name='talk')
    op.drop_table('talk')
    op.drop_index(op.f('ix_person_user_name'), table_name='person')
    op.drop_index(op.f('ix_person_mail'), table_name='person')
    op.drop_index(op.f('ix_person_id'), table_name='person')
    op.drop_table('person')
    op.drop_index(op.f('ix_conference_title'), table_name='conference')
    op.drop_index(op.f('ix_conference_start_date'), table_name='conference')
    op.drop_index(op.f('ix_conference_id'), table_name='conference')
    op.drop_index(op.f('ix_conference_end_date'), table_name='conference')
    op.drop_index(op.f('ix_conference_description'), table_name='conference')
    op.drop_table('conference')
    # ### end Alembic commands ###