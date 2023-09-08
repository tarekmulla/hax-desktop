"""Module of the main application form"""
from tkinter import PhotoImage

from customtkinter import CTk

from classes.gui.enums import Windows
from gui.about_frame import AboutFrame
from gui.main_menu import MainMenu
from gui.menubar import MenuBar
from gui.setting_frame import SettingFrame
from gui.sqli_frame import SqliFrame
from gui.xss_frame import XssFrame
from utilities.config import get_app_initial_size, get_icon
from utilities.log import LogLevel, log_msg


class App(CTk):
  """The main application window"""
  def __init__(self):
    super().__init__()
    self.main_menu = MainMenu(master=self)
    self.menubar = MenuBar(master=self)
    self.__init_components__()
    self.is_ready = True

  def __init_components__(self):
    """Initialize the main form GUI components"""
    self.title("HaX Cybersecurity tool")
    self.geometry(get_app_initial_size())
    self.resizable(True, True)

    # Set the application icon
    photo = PhotoImage(file=get_icon())
    self.iconphoto(False, photo)

    # init the menubar and its components
    self.menubar.init_items()
    self.configure(menu=self.menubar)

    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=0)
    self.grid_rowconfigure(0, weight=1)

    # init the main menu and place it in hte main window
    self.main_menu.init_items(self._fill_frame)
    self.main_menu.grid(column=0, row=0, sticky="nsew")

    # No frame is showing when app launch
    self.current_frame = None

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
    log_msg(f"{window} frame opened", LogLevel.INFO)

  def run(self):
    """run the main application interface"""
    log_msg("Application Start")
    self.mainloop()
    log_msg("Application End")
