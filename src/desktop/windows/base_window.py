"""Base class for child windows in the application"""
from customtkinter import CTk, CTkToplevel

from ..frames.base_frame import BaseFrame


class BaseWindow(CTkToplevel):
  """Base class for child windows in the application"""

  def __init__(self, master: CTk, size: str, title: str):
    self.master = master
    super().__init__(master)
    self.title(title)
    self.geometry(size)
    self.resizable(False, False)
    self.master.eval(f'tk::PlaceWindow {str(self)} center')

    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)
    self._init_main_frame()

    self.set_default_input()
    self.is_ready = True

  def _init_main_frame(self):
    self.main_frame = BaseFrame(self)
    self.main_frame.grid(row=0, column=0, sticky="news")

  def set_default_input(self):
    """Set default value for the window widgets"""
    self.main_frame.set_default_input()
