import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative
import os


Base  = sqlalchemy.ext.declarative.declarative_base()
# Read all secret values for connection string from env
# Please change alembic connection string in alembic.ini based on this setting from env
connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
    os.getenv('DB_USERNAME'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_NAME')
)
engine = sa.create_engine(connection_string)

db_session = orm.scoped_session(orm.sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base.query = db_session.query_property()

# lazyload = orm.lazyload
# joinedload = orm.joinedload