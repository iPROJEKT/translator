import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker

load_dotenv()

host = str(os.getenv("HOST"))
password = str(os.getenv("PASSWORD"))
database = str(os.getenv("DATABASE"))

engine = create_engine(f"postgresql+psycopg2://postgres:{password}@{host}/{database}")

session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()
