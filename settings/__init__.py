import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
load_dotenv(verbose=True)
env_path = Path("../") / ".env"
load_dotenv(dotenv_path=env_path)

DOMAIN = os.getenv("API_DOMAIN")
SPORTSMAN_LIST_URL = os.getenv("SPORTSMAN_LIST_URL")
WRITE_WEIGHTS_URL = os.getenv("WRITE_WEIGHTS_URL")
