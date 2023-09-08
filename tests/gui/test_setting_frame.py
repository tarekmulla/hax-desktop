

from gui.setting_frame import SettingFrame

from . import FakeWindow


def test_setting_frame():
  """Test creating setting frame"""
  main_window = FakeWindow()
  setting_frame = SettingFrame(main_window)
  assert setting_frame.is_ready
