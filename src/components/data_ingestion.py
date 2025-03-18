import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    '''
    Configuration class for data ingestion paths.
    Defines default paths for storing raw, train, and test data.
    '''

    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')


class DataIngestion:
    '''
    Class responsible for data ingestion process.
    Reads data from the specified source, splits it into training and testing sets,
    and saves them as CSV files.
    '''

    def __init__(self):
        '''
        Initializes the DataIngestion class with default configuration.
        '''
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        '''
        Executes the data ingestion process:
        - Reads data from a CSV file
        - Splits it into training and testing datasets
        - Saves these datasets to specified paths
        
        Returns:
            tuple: Paths to the train and test datasets
        '''

        logging.info('Entered the data ingestion method or component')
        try:
            # Reading dataset into pandas dataframe
            df = pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as a Dataframe')

            # Create the directory if don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)


            logging.info('Train Test split initiated')

            # Splitting dataset into train and test sets (80-20 split)    
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            # Saving dataset into CSV files
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed.')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # raise the customexception for better debugging
            raise CustomException(e,sys)
        
if __name__=='__main__':
    # create the DataIngestion object and Initiate data ingestion
    obj = DataIngestion()
    obj.initiate_data_ingestion()