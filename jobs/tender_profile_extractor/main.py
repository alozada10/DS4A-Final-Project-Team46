# basic imports
import warnings
import pandas as pd

# local imports
from jobs.tender_profile_extractor.tasks import pdf_to_txt, make_preditction
from jobs.tender_profile_extractor import settings
from utils import file_manager

# Omit warnings
warnings.filterwarnings(settings.WARNINGS)

if __name__ == '__main__':
    pdf_to_txt.convert_documents_to_txt(path=settings.TENDERS_PATH,
                                        resolution=500)
    print('Se convirtió a txt')

    file_manager.get_all_pages(path=settings.TENDERS_PATH,
                               save_dir_path=settings.DATA_FRAMES_PATH,
                               name=settings.ALL_PAGES_DF_NAME)
    print('Se crea bien el df con todas las pages')

    x = pd.read_csv(settings.DATA_FRAMES_PATH+settings.ALL_PAGES_DF_NAME)

    tenders = x.TENDER_ID.unique()

    final_prediction = None
    for tender in tenders:
        x_temp = x[x.TENDER_ID == tender]

        prediction = make_preditction.predict(x=x_temp,
                                              model_path=settings.MODEL_PATH + '/' + settings.MODEL_NAME)
        print('Se hizo bien una prediction para '+str(tender))

        top_numbers = prediction.sort_values(by='NUMBER', ascending=False).NUMBER.unique()[:settings.TOP_NUMBER_PAGES]
        prediction['PRED'] = [0] * prediction.shape[0]
        prediction['PRED'][prediction.NUMBER.isin(top_numbers)] = 1

        final_prediction = pd.concat([final_prediction, prediction])

    final_prediction.to_csv(settings.DATA_FRAMES_PATH + '/' + settings.RESULTS_NAME)
    print('Se guardaron las predicciones')
