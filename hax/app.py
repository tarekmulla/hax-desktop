"""Module of the main application form"""
from os.path import dirname
from tkinter import PhotoImage, Tk

from classes.enums import Windows
from config import AppConfig
from frames.about_frame import AboutFrame
from frames.main_menu import MainMenu
from frames.menubar import MenuBar
from frames.setting_frame import SettingFrame
from frames.sqli_frame import SqliFrame
from frames.xss_frame import XssFrame


class App(Tk):
  """The main application window"""
  def __init__(self):
    self.base_dir = dirname(__file__)
    super().__init__()
    self.app_config = AppConfig()
    self.main_menu = MainMenu(master=self)
    self.menubar = MenuBar(master=self)
    self.__init_components__()
    self.current_frame = None

  def __init_components__(self):
    """Initialize the main form GUI components"""
    self.title("HaX Cybersecurity tool")
    self.geometry(self.app_config.get_app_initial_size())
    self.resizable(False, False)

    # Set the application icon
    photo = PhotoImage(file=self.app_config.get_icon())
    self.iconphoto(False, photo)

    # init the menubar and its components
    self.menubar.init_items()
    self.configure(menu=self.menubar)

    # init the main menu and place it in hte main window
    self.main_menu.init_items(self._fill_frame)
    self.main_menu.grid(column=0, row=0, sticky="nsw")

  def _fill_frame(self, event, window: Windows):
    # pylint: disable=unused-argument
    """Fill a frame into the main window when the user select window"""

    # destroy the old frame
    if self.current_frame:
      self.current_frame.destroy()
      self.current_frame = None

    # initialize the new frame
    if window == Windows.XSS:
      self.current_frame = XssFrame(self)
    elif window == Windows.SQLI:
      self.current_frame = SqliFrame(self)
    elif window == Windows.SETTING:
      self.current_frame = SettingFrame(self)
    elif window == Windows.ABOUT:
      self.current_frame = AboutFrame(self)
    else:
      raise NotImplementedError(f"The frame '{window}' hasn't implemented yet")

    # show the frame into the main window
    self.current_frame.grid(row=0, column=1, sticky="nsew")

  def run(self):
    """run the main application interface"""
    self.mainloop()
