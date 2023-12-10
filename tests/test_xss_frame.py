from haxdesktop.frames.xss_frame import XssFrame

from . import FakeWindow


def test_xss_frame():
  """Test creating XSS frame"""
  main_window = FakeWindow()
  xss_frame = XssFrame(main_window)
  assert xss_frame.is_ready
