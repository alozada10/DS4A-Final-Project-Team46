# basic imports
import warnings
import pandas as pd

# local imports
from jobs.tender_profile_extractor.tasks import pdf_to_txt, make_preditction
from jobs.tender_profile_extractor import settings
from utils import file_manager

# omit warnings
warnings.filterwarnings(settings.WARNINGS)


def main(path: str = settings.TENDERS_PATH,
         resolution: int = 500,
         save_dir_path: str = settings.DATA_FRAMES_PATH,
         name: str = settings.ALL_PAGES_DF_NAME,
         model: str = settings.MODEL_PATH,
         model_name: str = settings.MODEL_NAME,
         top_number_pages: int = settings.TOP_NUMBER_PAGES,
         data_frames_path: str = settings.DATA_FRAMES_PATH,
         results_name: str = settings.RESULTS_NAME):

    pdf_to_txt.convert_documents_to_txt(path=path,
                                        resolution=resolution)
    print('Se convirtió a txt')

    file_manager.get_all_pages(path=path,
                               save_dir_path=save_dir_path,
                               name=name)
    print('Se crea bien el df con todas las pages')

    x = pd.read_csv(data_frames_path + '/' + name)

    print(x.columns)

    tenders = x.TENDER_ID.unique()

    print(tenders)

    final_prediction = None
    for tender in tenders:
        x_temp = x[x.TENDER_ID == tender]

        prediction = make_preditction.predict(x=x_temp,
                                              model_path=model + '/' + model_name)
        print('Se hizo bien una prediction para ' + str(tender))

        top_numbers = prediction.sort_values(by='NUMBER', ascending=False).NUMBER.unique()[:top_number_pages]
        prediction['PRED'] = [0] * prediction.shape[0]
        prediction['PRED'][prediction.NUMBER.isin(top_numbers)] = 1
        prediction['PRED'][prediction.NUMBER == 0] = 0

        final_prediction = pd.concat([final_prediction, prediction])

    final_prediction.to_csv(data_frames_path + '/' + results_name)
    print('Se guardaron las predicciones')
