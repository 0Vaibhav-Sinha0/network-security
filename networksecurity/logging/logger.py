'''This module sets up logging for the network security project. It configures the logging system to create log files in a structured manner, with each log file named based on the current date and time. The logs are stored in a "logs" directory within the current working directory. The logging format includes timestamps, line numbers, logger names, log levels, and messages. This setup allows for effective tracking of events and debugging throughout the project.'''

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)