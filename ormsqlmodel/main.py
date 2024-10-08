from fastapi import FastAPI, Body, Query, Path  # type: ignore
import uvicorn  # type: ignore
from sqlmodel import SQLModel, create_engine, select, Field, Session  # type: ignore
connection_string = 'DB_URL'
connection = create_engine(connection_string)

app = FastAPI()

class Students(SQLModel, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    is_active: bool

# Create the tables in the database
SQLModel.metadata.create_all(connection)



#
# Add a simple route for testing
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}




@app.get("/getStudents")
def get_students():
    with Session(connection) as session:
        statement = select(Students)
        result = session.execute(statement)
        data = result.scalars().all()  # .all() fetches all records as a list
        return data
    
    
@app.get("/getSingleStudents")
def get_single_students():
    with Session(connection) as session:
        statement = select(Students).where(Students.name=="Bassam")
        result = session.execute(statement)
        data = result.scalars().all()  # .all() fetches all records as a list
        return data

# a start function to run the application
def start():
    uvicorn.run("ormsqlmodel.main:app", host="127.0.0.1", port=8000, reload=True)


