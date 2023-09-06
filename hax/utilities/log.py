"""All logging operations"""
import logging
from datetime import datetime
from os import makedirs
from os.path import isdir, join

from utilities.config import AppConfig


def init_log(app_config: AppConfig):
  """init logging"""
  logs_dir = join(app_config.base_dir, app_config.log['folder'])
  if not isdir(logs_dir):
    makedirs(logs_dir)
  file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S.log")
  log_file_path = join(logs_dir, file_name)
  logging.basicConfig(filename=log_file_path, level=app_config.log["level"])


def log(message):
  """log message"""
  logging.info(message)
