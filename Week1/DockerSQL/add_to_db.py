import os
import pandas as pd
from sqlalchemy import create_engine


def add_postgre_trip(file, name):
    engine = create_engine(f'postgresql://root:root@localhost:5432/ny_taxi')
    df_max = pd.read_csv(file, iterator=True, chunksize=100000)

    df_mini = next(df_max)
    df_mini.tpep_pickup_datetime = pd.to_datetime(df_mini.tpep_pickup_datetime)
    df_mini.tpep_dropoff_datetime = pd.to_datetime(df_mini.tpep_dropoff_datetime)

    df_mini.head(n=0).to_sql(name=name, con=engine, if_exists='replace')
    df_mini.to_sql(name=name, con=engine, if_exists='append')

    while True:
        df_mini = next(df_max)
        df_mini.tpep_pickup_datetime = pd.to_datetime(df_mini.tpep_pickup_datetime)
        df_mini.tpep_dropoff_datetime = pd.to_datetime(df_mini.tpep_dropoff_datetime)

        df_mini.to_sql(name=name, con=engine, if_exists='append')


def add_postgre_lookup(file, name):
    engine = create_engine(f'postgresql://root:root@localhost:5432/ny_taxi')
    df_max = pd.read_csv(file)

    df_max.head(n=0).to_sql(name=name, con=engine, if_exists='replace')
    df_max.to_sql(name=name, con=engine, if_exists='append')


if __name__ == '__main__':
    # get current directory details to check the Data directory
    path = f'{os.getcwd()}/Data'
    check_dir = os.listdir(path)

    add_postgre_trip(f'{os.getcwd()}/Data/{check_dir[0]}', check_dir[0][:-4])
    add_postgre_lookup(f'{os.getcwd()}/Data/{check_dir[1]}', check_dir[1][:-4])

    # test =pd.read_csv(f'{os.getcwd()}/Data/{check_dir[0]}')
    # print(test.shape[0])
