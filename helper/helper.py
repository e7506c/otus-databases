import psycopg2
from dataclasses import dataclass, asdict
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DATABASE_NAME = 'test_database'
TABLE_NAME = 'persons'


@dataclass
class MyDbConfig:
    host: str = 'localhost'
    port: str = '3306'
    user: str = 'mysql_user'
    password: str = 'mysql_password'
    database: str = DATABASE_NAME

    def asdict(self) -> dict:
        return asdict(self)

    def db_url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


@dataclass
class PgDbConfig:
    host: str = 'localhost'
    port: str = '5432'
    user: str = 'postgres'
    password: str = 'postgres'
    database: str = DATABASE_NAME

    def asdict(self) -> dict:
        return asdict(self)

    def db_url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


connection = psycopg2.connect(**PgDbConfig().asdict())

# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor object
cursor = connection.cursor()


def select_from_table(cursor):
    cursor.execute(f'SELECT * FROM {TABLE_NAME};')
    results = cursor.fetchall()

    print(f"\033[92m---> All rows from table '{TABLE_NAME}':\033[0m")
    for row in results:
        print(f'\033[94m{row}\033[0m')
