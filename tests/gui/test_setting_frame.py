

from gui.windows.setting_window import SettingWindow

from . import FakeWindow


def test_setting_frame():
  """Test creating setting frame"""
  main_window = FakeWindow()
  setting_frame = SettingWindow(main_window)
  assert setting_frame.is_ready
