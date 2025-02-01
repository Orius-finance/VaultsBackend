import os
import dotenv

dotenv.load_dotenv()

def get_env_key(key: str):
    return os.getenv(key)
