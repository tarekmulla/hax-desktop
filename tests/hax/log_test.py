"""Unit tests for the config class"""

import pytest
from utilities.log import LOGGER, LOGGER_FILE, init_log, log_msg


def test_logging_message():
  message = "Hello World"
  init_log()
  log_msg(message)
  with open(LOGGER_FILE) as file:
    log_messages = file.read()
  assert message in log_messages
