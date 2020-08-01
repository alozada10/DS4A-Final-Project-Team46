# local imports
from jobs.tender_profile_extractor import main as main_back
from jobs.tender_profile_extractor import settings
from utils import file_manager as fm
from utils import plot_info as pi

from dash.dependencies import Input, Output, State

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import os
import pandas as pd
import base64
from app import app

UPLOAD_DIRECTORY = settings.TENDERS_PATH_FRONT

from lib import title, pictures, upload

#############################################################
if __name__ == "__main__":
    main_back.main()
