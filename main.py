from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline



STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Data Validation stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation= DatavalidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)
    raise e





