

from haxdesktop.frames.setting.cloud import CloudSettingFrame

from . import FakeWindow


def test_setting_frame():
  """Test creating setting frame"""
  main_window = FakeWindow()
  setting_frame = CloudSettingFrame(main_window)
  assert setting_frame.is_ready
