from sqlmodel import SQLModel, create_engine, select, Field, Session  # type: ignore
import os



#E58rnAfdhRLmEXme
# Define the connection string
connection_string = os.getenv('DB_URL')
connection = create_engine(connection_string)


def create_tables():
    # Create the tables in the database
    SQLModel.metadata.create_all(connection)