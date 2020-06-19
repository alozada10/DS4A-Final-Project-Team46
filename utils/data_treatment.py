# Decimals must be float
import pandas
import logging
from jobs.user_value_propen.targets.snowflake_target_factory import SnowflakeTargetFactory

snowflake_target = SnowflakeTargetFactory.build()


# Remove_outliers
def remove_outlier(df_in: pandas.DataFrame = None,
                   col_name: str = None) -> pandas.DataFrame:
    q1 = df_in[col_name].quantile(0.05)
    q3 = df_in[col_name].quantile(0.95)
    iqr = q3 - q1  # Interquartile range
    fence_low = q1 - 1.5 * iqr
    fence_high = q3 + 1.5 * iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]

    return df_out


# Nan_Numeric
def nan_numeric(db: pandas.DataFrame = None,
                num_list: list = None) -> pandas.DataFrame:
    sentinel = False
    for i in num_list:
        if db[str(i)].isnull().all():
            db[str(i)].fillna(0, inplace=True)
            logging.warning(f'Daily feature ' + str(i) + ' has all values in null')
            sentinel = True
        else:
            db[str(i)].fillna(round(db[str(i)].mean()), inplace=True)
    
    if sentinel:
        resp = snowflake_target.upload_data(df=db[num_list],
                                            schema='BR_WRITABLE',
                                            table_name='hvu_data_warnings',
                                            if_exists='append'
                                            )

    return db


# Nan_Cate
def nan_cate(db: pandas.DataFrame = None,
             cat_list: list = None,
             replacement: str = 'Otro') -> pandas.DataFrame:
    sentinel = False
    for i in cat_list:
        if db[str(i)].isnull().all():
            db[str(i)].fillna(replacement, inplace=True)
            logging.warning(f'Daily feature ' + str(i) + ' has all values in null')
            sentinel = True
        else:
            db[str(i)].fillna(replacement, inplace=True)

    if sentinel:
        resp = snowflake_target.upload_data(df=db[cat_list],
                                            schema='BR_WRITABLE',
                                            table_name='hvu_data_warnings',
                                            if_exists='append'
                                            )

    return db
