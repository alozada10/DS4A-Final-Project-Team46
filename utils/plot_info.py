import pandas as pd
import ast


def prepare_info(results_df: pd.DataFrame = None) -> pd.DataFrame:
    result = []
    for i in results_df.PROFESSIONS.values:
        x = ast.literal_eval(i)
        x = [n.strip() for n in x]
        result += x
    graph = pd.DataFrame(data={'profession': result})
    graph['count'] = [0] * graph.shape[0]
    graph = pd.pivot_table(index='profession', aggfunc='count', data=graph).reset_index().sort_values(by='count',
                                                                                                      ascending=False)
    return graph
