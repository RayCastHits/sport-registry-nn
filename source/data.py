from .services import get_json
from .cleaning import get_clean_primary_data, get_clean_medical_data
from .settings import SPORTSMAN_LIST_URL

DATA = get_json(SPORTSMAN_LIST_URL)
CLEAN_PRIMARY_DATA = get_clean_primary_data(DATA)
CLEAN_MEDICAL_DATA = get_clean_medical_data(DATA)
