"""Unit tests for the config class"""

from utilities.log import LOGGER_FILE, init_log, log_msg


def test_logging_message():
  """Test logging message using log system"""
  message = "Hello World"
  init_log()
  log_msg(message)
  with open(LOGGER_FILE, mode="r", encoding="utf-8") as file:
    log_messages = file.read()
  assert message in log_messages
