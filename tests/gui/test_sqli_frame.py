from gui.sqli_frame import SqliFrame

from . import FakeWindow


def test_sqli_frame():
  """Test creating SQLi frame"""
  main_window = FakeWindow()
  xss_frame = SqliFrame(main_window)
  assert xss_frame.is_ready
