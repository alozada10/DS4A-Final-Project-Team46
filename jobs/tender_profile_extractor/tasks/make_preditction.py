import spacy
from utils import file_manager as fm
import pandas as pd


def extract_profession(text: str = None,
                       model_path: str = None) -> (list, int):
    nlp = spacy.load(model_path)
    nlp_page = nlp(text)
    professions = [str(i).lower().replace(',', '').replace('.', '').replace(';', '') for i in nlp_page.ents]
    size = len(nlp_page.ents)

    return professions, size


def predict(x: pd.DataFrame = None,
            model_path: str = None) -> pd.DataFrame:
    resp = {}
    x = x.reset_index().drop(columns='index')
    for i in range(x.shape[0]):
        temp = x[x.index == i]
        tender = temp.TENDER_ID.values[0]
        document = temp.DOCUMENT_ID.values[0]
        page = temp.PAGE_ID.values[0]

        path = fm.get_path(tender_id=tender,
                           document_id=document,
                           page_id=page)

        key = '/'.join(path.split('/')[-3:])
        f = open(path, "r")
        page = f.read()
        professions, size = extract_profession(text=page,
                                               model_path=model_path)
        value = (professions, size)
        resp[key] = value

    prediction = pd.DataFrame(resp).T.reset_index().rename(columns={0: 'PROFESSIONS', 1: 'NUMBER', 'index': 'PATH'})
    prediction['TENDER_ID'] = [int(i.split('/')[0]) for i in prediction.PATH]
    prediction['DOCUMENT_ID'] = [int(i.split('/')[1]) for i in prediction.PATH]
    prediction['PAGE_ID'] = [int(i.split('/')[2].split('_')[1].split('.')[0]) for i in prediction.PATH]
    prediction = prediction.sort_values(by=['TENDER_ID', 'DOCUMENT_ID', 'NUMBER'], ascending=[True, True, False])

    return prediction

