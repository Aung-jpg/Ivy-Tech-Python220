import sqlalchemy

engine = sqlalchemy.create_engine(r'C:\Users\aung512x01\Desktop\Aung Programs\IvyTech-Python\Module-4\API\books.db')

# Create a metadata object
metadata = sqlalchemy.MetaData()

# Reflect the existing book table
books_table = sqlalchemy.Table('book', metadata, autoload_with=engine)

# Create a select statement
stmt = sqlalchemy.sql.select(books_table.c.title).order_by(books_table.c.title)

# Execute the statement and fetch the results
with engine.connect() as connection:
    result = connection.execute(stmt)
    for row in result:
        print(row.title)