import pandas as pd
import os


def get_file_from_url(file: str, file_name: str):
    current_file = pd.read_csv(file)
    current_file.to_csv(f'Data/{file_name}')


if __name__ == '__main__':
    # get current directory details to check the Data directory
    path = f'{os.getcwd()}/Data'
    check_dir = os.listdir(path)

    # if directory is empty then get the files from the web and store it in the folder
    if len(check_dir) == 0:
        get_file_from_url('https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv',
                          'yellow_tripdata_2021-01.csv')
        get_file_from_url('https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv', 'taxi+_zone_lookup.csv')
    # if not empty then end because files are available
    else:
        print("Files are in Data directory")
