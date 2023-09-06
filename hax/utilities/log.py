"""All logging operations"""
import logging
from datetime import datetime
from os import makedirs
from os.path import isdir, join

from utilities.config import BASE_DIR, LOG


def init_log():
  """init logging"""
  logs_dir = join(BASE_DIR, LOG['folder'])
  if not isdir(logs_dir):
    makedirs(logs_dir)
  file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S.log")
  log_file_path = join(logs_dir, file_name)
  logging.basicConfig(filename=log_file_path, level=LOG["level"])


def log(message):
  """log message"""
  logging.info(message)
