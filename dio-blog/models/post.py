import sqlalchemy as sa
from database import metadata

posts = sa.Table('posts', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(100), nullable=False, unique=True),
    sa.Column('published_at', sa.DateTime),
    sa.Column('published', sa.Boolean, default=False),
    sa.Column('content', sa.Text, nullable=False),

)


