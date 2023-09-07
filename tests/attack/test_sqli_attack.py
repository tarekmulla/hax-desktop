"""Test class for Utilities methods"""


from os import remove
from time import sleep
from unittest.mock import MagicMock

from classes.attacks.attack_manager import AttackManager
from classes.attacks.enums import AttackType, RequestType

from .. import TEST_DIR


def test_xss_attack():
  test_file = f"{TEST_DIR}/attack/payloads.txt"
  with open(test_file, mode="w", encoding="utf-8") as file:
    file.write("TEST1\nTEST2")

  mock_response = MagicMock()
  mock_response.status_code = 200

  manager = AttackManager("https://test.com", RequestType.GET, "", "", AttackType.SQLI)
  manager._send_http_request = MagicMock()
  # mock the context manager of the _send_http_request method ("with" statment)
  manager._send_http_request.return_value.__enter__.return_value = mock_response

  frame_mock = MagicMock()
  manager.start(test_file, frame_mock.add_result)
  # allow sometime for the thread to finish
  while not manager.is_finish:
    sleep(0.1)
  remove(test_file)

  assert manager._send_http_request.call_count == 2
