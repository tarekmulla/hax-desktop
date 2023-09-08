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
    self.rowconfigure(0, weight=2)
    self.rowconfigure((1, 2), weight=1)

    img_logo = self.add_image(get_logo(), size=(300, 160))
    img_logo.grid(row=0, column=0, pady=(0, 10), sticky="news")
    self.add_label(about, justify="center").grid(row=1, column=0)
    self.add_link(link, link).grid(row=2, column=0, pady=(0, 50))
