import os
from jobs.tender_profile_extractor import settings
import pandas as pd


# Gets path
def get_path(tender_id: int = None,
             document_id: int = None,
             page_id: int = None,
             path: str = settings.TENDERS_PATH) -> str:
    path = "{}/{}/{}/page_{}.txt".format(path, str(tender_id), str(document_id), str(page_id))

    return path


def get_all_pages(path: str = settings.TENDERS_PATH,
                  save_dir_path: str = settings.DATA_FRAMES_PATH,
                  name: str = settings.ALL_PAGES_DF_NAME):
    result = None
    for roots, dirs, files in os.walk(path, topdown=False):
        for document in files:
            if 'page' in document:
                roots = roots.replace('\\', '/')
                single_page = roots.replace('\\', '/') + '/' + document

                tender_id = int(single_page.split('/')[-3:][0])
                document_id = int(single_page.split('/')[-2:][0])
                page = int(single_page.split('/')[-1:][0].split('_')[1].split('.')[0])

                temp = pd.DataFrame([[tender_id, document_id, page]], columns=['TENDER_ID', 'DOCUMENT_ID', 'PAGE_ID'])

                result = pd.concat([result, temp])

    if not os.path.exists(save_dir_path):
        os.makedirs(save_dir_path)

    result = result.reset_index().drop(columns='index')
    result.to_csv(save_dir_path + '/' + name, index=False)