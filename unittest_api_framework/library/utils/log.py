import os
import logging
import logging.handlers
import sys

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s")
LOG_FILE = "test_log.log"
LOG_FOLDER = 'logs'
BASE_FOLDER = '/Users/gaurav.mishra/framework'

def get_log_path(log_file=LOG_FILE):
   return os.path.join(BASE_FOLDER, LOG_FOLDER, log_file)

def get_file_handler():
   log_path = get_log_path()
   file_handler = logging.handlers.WatchedFileHandler(log_path)
   file_handler.setFormatter(FORMATTER)
   file_handler.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
   return file_handler

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   console_handler.setLevel(logging.DEBUG)
   return console_handler

def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger

testlog = get_logger("my_test_logs")
testlog.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
testlog.info('123')