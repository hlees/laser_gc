
import psycopg2
from psycopg2 import extensions, OperationalError, connect


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ..common_config import database_url


engine = create_engine(database_url, pool_size=20, max_overflow=-1)
DB = scoped_session(sessionmaker(bind=engine))


