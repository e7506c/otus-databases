from helper.helper import cursor, connection, TABLE_NAME


create_table_stmt = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL
);
"""

cursor.execute(create_table_stmt)

cursor.execute(f"SELECT * FROM {TABLE_NAME};")
# Fetch the results
results = cursor.fetchall()
if results:
    for row in results:
        print(row)
else:
    print(f'Table {TABLE_NAME} is empty!')

connection.commit()

cursor.close()
connection.close()
