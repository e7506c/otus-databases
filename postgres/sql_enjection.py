from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from helper.helper import connection, cursor, TABLE_NAME

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

insert_stmt = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s);'
cursor.execute(insert_stmt, ('Alice', 20))
cursor.execute(insert_stmt, ('Bob', 30))

# 1' or 1=1;--
# 1';delete from persons;--
# 1';drop table persons;--
while True:
    some_name = input('insert name: ')
    if 'exit' in some_name:
        break

    sql_stmt = f"SELECT * FROM {TABLE_NAME} WHERE name='{some_name}'"
    try:
        cursor.execute(sql_stmt)
        results = cursor.fetchall()

        for row in results:
            print(row)
    except Exception as err:
        print(err)
