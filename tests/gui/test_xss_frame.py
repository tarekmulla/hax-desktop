from tkinter import Tk

from gui.xss_frame import XssFrame


def test_xss_frame():
  """Test creating XSS frame"""
  main_window = Tk()
  xss_frame = XssFrame(main_window)
  assert xss_frame.is_ready
