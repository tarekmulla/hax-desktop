"""About frame to show information about the application"""
from gui.base_frame import BaseFrame
from utilities.config import GENERAL, get_logo


class AboutFrame(BaseFrame):
  """About frame to show information about the application"""
  def __init__(self, master):
    super().__init__(master, "About HaX")

  def __init_frame__(self):
    super().__init_frame__()
    link = GENERAL["domain"]
    about = GENERAL["about"]

    self.columnconfigure(0, weight=1)
    self.add_image(get_logo(), 0, 0, pady=(25, 0))
    self.add_label(about, justify="center", wraplength=550).grid(row=1, column=0)

    self.add_link(link, link, 2, 0)
    self.add_link(link, link, 2, 0)
