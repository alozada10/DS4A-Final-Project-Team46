import os

APP_VERSION = 'v1.0.0'
APP = 'growth-ai'
APP_ID = os.getenv('x_application_id', APP)

WARNINGS = 'ignore'

TENDERS_PATH = '../../../app_data/tenders'
POPPLER_PATH = '../../../app_data/wml/bin'
TESSERACT_PATH = '../../../app_data/wml/tesseract.exe'
DATA_FRAMES_PATH = '../../../app_data/data_frames'
ALL_PAGES_DF_NAME = 'all_pages.csv'
MODEL_PATH = '../../../app_data/model'
MODEL_NAME = 'cnc_profesiones_cargos_2020-07-17'
TOP_NUMBER_PAGES = 3
RESULTS_NAME = 'predictions.csv'
TENDERS_PATH_FRONT = '../../../app_data/tenders'


