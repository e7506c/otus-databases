from dataclasses import dataclass, asdict


@dataclass
class MongoConfig:
    host: str = 'localhost'
    port: str = '27017'
    user: str = 'mongo_user'
    password: str = 'mongo_password'

    def asdict(self) -> dict:
        return asdict(self)

    def db_url(self):
        return f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}'
