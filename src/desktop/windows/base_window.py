"""Base class for child windows in the application"""
from customtkinter import CTk, CTkToplevel

from ..frames.base_frame import BaseFrame


class BaseWindow(CTkToplevel):
  """Base class for child windows in the application"""

  def __init__(self, master: CTk, width: int, height: int, title: str):
    self.master = master
    super().__init__(master)
    self.title(title)
    self.__set_position(master, width, height)
    self.resizable(False, False)

    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)
    self._init_main_frame()

    self.set_default_input()
    self.is_ready = True

  def __set_position(self, master: CTk, width, height):
    x_cordinate = int(master.winfo_x() + (master.winfo_width()//2) - (width//2))
    y_cordinate = int(master.winfo_y() + (master.winfo_height()//2) - (height//2))
    self.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

  def _init_main_frame(self):
    self.main_frame = BaseFrame(self)
    self.main_frame.grid(row=0, column=0, sticky="news")

  def set_default_input(self):
    """Set default value for the window widgets"""
    if hasattr(self, "main_frame"):
      self.main_frame.set_default_input()
