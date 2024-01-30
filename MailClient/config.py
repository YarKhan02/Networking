from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sender_email: str
    reciever_email: str
    password: str

    class Config:
        env_file = '.env'

settings = Settings()