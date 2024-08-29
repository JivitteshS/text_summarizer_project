from src.textSummarizer.config.configuration import ConfugurationManager
from src.textSummarizer.components.data_validation import DataValidation
from src.textSummarizer.logging import logger
from src.textSummarizer.components.data_ingestion import DataIngestion


class DatavalidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfugurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()

        

