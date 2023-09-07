from tkinter import Tk

from gui.setting_frame import SettingFrame


def test_setting_frame():
  """Test creating setting frame"""
  main_window = Tk()
  setting_frame = SettingFrame(main_window)
  assert setting_frame.is_ready
