
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
metadata_obj = MetaData()

POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5555
POSTGRES_DB = "sqlalchemy-test"
POSTGRES_USER = "db-user"
POSTGRES_PASSWORD = "password"
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

print ("creating engine....")
engine = create_engine(DATABASE_URL)
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
print ("engine created", engine)


# Define and create metadata
from sqlalchemy import MetaData
metadata_obj = MetaData()

from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

from sqlalchemy import ForeignKey
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)


metadata_obj.create_all(engine)  # Creates the tables