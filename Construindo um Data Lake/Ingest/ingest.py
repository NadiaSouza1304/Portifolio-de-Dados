from datetime import datetime
from sqlalchemy import create_engine
from configparser import ConfigParser
import boto3
import pandas as pd
import os

class Ingestion:

    def __init__(self, subject):
        self.__subject = subject
        self.__ts_proc = datetime.now().strftime('%Y%m%d%H%M%S')
        self.__ref_proc = datetime.now().strftime('%Y%m%d')
        self.__filename = f'{self.__subject}_{self.__ref_proc}_{self.__ts_proc}'
        self.__config = self.__get_config()

    def __get_config(self):
        config = ConfigParser()
        config_dir = os.getcwd() + '/config/config.cfg'
        config.read(config_dir)

        return config
        
    def __create_engine(self):
        user = self.__config.get('DB','user')
        password = self.__config.get('DB','password')
        host = self.__config.get('DB','host')
        database = self.__config.get('DB','database')

        connection_string = f'postgresql://{user}:{password}@{host}/{database}'
    
        engine = create_engine(connection_string)

        return engine.connect()
    
    def __get_db_data(self):
        query = f'SELECT * FROM public.{self.__subject}'
        print(query)
        df = pd.read_sql(query, self.__create_engine())
        df.to_csv(f'{self.__filename}.csv', index=False)

    def __upload_to_s3(self):
        s3_client = boto3.client('s3')
        bucket_name = 'data-lake-portifolio-211529015094'
        prefix = f'0000_ingestion/{self.__subject}/{self.__filename}.csv'
        print(prefix)

        try:
            with open(f'{self.__filename}.csv', 'rb') as f:
                s3_client.put_object(Bucket=bucket_name, Key=prefix, Body=f)

        except Exception as e:
            print(f'Erro!{e}')

    def __delete_file(self):
        cmd = f'rm {self.__filename}.csv'
        os.system(cmd)
    
    def start(self):
        self.__get_db_data()
        self.__upload_to_s3()
        self.__delete_file()

if __name__ == '__main__':
    ingest = Ingestion('users')
    ingest.start()