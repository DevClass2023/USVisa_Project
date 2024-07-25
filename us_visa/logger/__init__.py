import logging
import os
from from_root import from_root
from datetime import datetime

# Define the log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for logs
log_dir = 'logs'

# Get the path for the logs directory using from_root()
logs_path = os.path.join(from_root(), log_dir)

# Create the logs directory if it does not exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
log_file_path = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Test logging
logging.debug("Debug logging is enabled.")
logging.info("Logging setup complete.")
logging.warning("This is a warning.")
logging.error("An error occurred.")
logging.critical("Critical issue!")
