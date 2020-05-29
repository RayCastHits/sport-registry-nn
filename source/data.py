from .services import get_json
from ..settings import SPORTSMAN_LIST_URL

DATA = get_json(SPORTSMAN_LIST_URL)
