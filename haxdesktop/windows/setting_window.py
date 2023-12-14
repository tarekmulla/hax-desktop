"""Setting Window"""
from haxcore.utilities.log import LogLevel, log_msg

from haxdesktop.classes.enums import Windows
from haxdesktop.frames.setting.apperance import AppearanceSettingFrame
from haxdesktop.frames.setting.cloud import CloudSettingFrame
from haxdesktop.frames.setting.general import GeneralSettingFrame
from haxdesktop.widgets.setting_menu import SettingMenu
from haxdesktop.windows.base_window import BaseWindow


class SettingWindow(BaseWindow):
  """Setting frame"""
  def __init__(self, root_window):
    super().__init__(root_window, 600, 400, "Setting")

  def _init_main_frame(self):
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=0)
    self.grid_rowconfigure(0, weight=1)

    # init the main menu and place it in the main window
    self.main_menu = SettingMenu(root_window=self)
    self.main_menu.init_items(self._fill_frame)
    self.main_menu.grid(column=0, row=0, sticky="nsew")

    # No frame is showing when app launch
    self.current_frame = None

  def _fill_frame(self, event, window: Windows):
    # pylint: disable=unused-argument
    """Fill a frame into the main window when the user select window"""
    if self.current_frame:
      self.current_frame.destroy()
      self.current_frame = None
    # initialize the new frame
    if window == Windows.CLOUD_SETTING:
      self.current_frame = CloudSettingFrame(self)
    elif window == Windows.GENERAL_SETTING:
      self.current_frame = GeneralSettingFrame(self)
    elif window == Windows.APPEARANCE_SETTING:
      self.current_frame = AppearanceSettingFrame(self)
    else:
      raise NotImplementedError(f"The frame '{window}' hasn't implemented yet")
    # show the frame into the main window
    self.current_frame.grid(row=0, column=1, sticky="nsew")

    log_msg(f"{window} opened", LogLevel.INFO)
