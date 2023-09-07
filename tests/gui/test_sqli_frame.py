from tkinter import Tk

from gui.sqli_frame import SqliFrame


def test_sqli_frame():
  """Test creating SQLi frame"""
  main_window = Tk()
  xss_frame = SqliFrame(main_window)
  assert xss_frame.is_ready
