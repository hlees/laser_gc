from flask import Flask, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.db = create_engine(database_url, pool_size=20, max_overflow=-1)
app.db.session = scoped_session(sessionmaker(bind=engine))
