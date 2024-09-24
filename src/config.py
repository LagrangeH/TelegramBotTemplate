from pydantic import conlist
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    redis_dsn: str
    admin_ids: conlist(int, min_length=1)

    postgres_user: str
    postgres_password: str
    postgres_db: str

    @property
    def database_url(self) -> str:
        return (f"postgresql://{self.db_user}:{self.db_password}"
                f"@db:5432/{self.db_name}")


settings = Settings()
