import logging
import os
from datetime import datetime

# Generate the log file with format MM_DD_YYYY_HH_MM_SS.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define directory path where log file will be stored
# Create a "logs" folder in current working directory
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)

# Create the log directory if not exist
os.makedirs(logs_path,exist_ok=True)

# Define the full log path for log file within the "logs" directory
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# Configure logging setting
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s %(message)s",
    level=logging.INFO  # Set the logging level to INFO (captures INFO, WARNING, ERROR, CRITICAL)
)
