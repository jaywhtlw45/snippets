from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session

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

# with engine.begin() as conn:
    # conn.execute(text("create table truck(year int, make varchar(50))"))
    # result = conn.execute(text("INSERT INTO car VALUES (24, 'toyota'), (25, 'Chevy'),(20, 'Ford')"))
    
    ## Select
    # result = conn.execute(text("SELECT year, make FROM car"))
    # for dict_row in result.mappings():
    #     print (dict_row)


# with engine.connect() as conn:
#     x = 5
#     y = 9
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
#     )
#     conn.commit()


stmt = text("SElECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x: {row.x}, y: {row.y}")