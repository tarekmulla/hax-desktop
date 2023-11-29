"""The main menu of the application"""
from customtkinter import CTkButton, CTkFrame, CTkImage
from PIL import Image

from core.classes.gui.enums import Windows
from core.utilities.config import get_image_path
from desktop.widgets.classes.menu_item import MenuItem


class SettingMenu(CTkFrame):
  """The setting menu of the application"""
  def __init__(self, master):
    self.master = master
    super().__init__(master, width=150, corner_radius=0)
    self.current_window = Windows.NONE

  def init_items(self, event_func):
    """Initialize the menu items"""
    self.menu_items = [
      MenuItem("General", "xss.png", Windows.GENERAL_SETTING),
      MenuItem("Appearance", "xss.png", Windows.APPEARANCE_SETTING),
      MenuItem("Cloud backend", "xss.png", Windows.CLOUD_SETTING)
    ]

    row = 0
    for item in self.menu_items:
      btn = self.create_menu_item(self, item.name, item.image, item.window, event_func)
      btn.grid(row=row, column=0, sticky="nsew")
      row = row + 1

  def mouse_click(self, event, window: Windows, click_event_func):
    """Call when a mouse click the menu item"""
    if self.current_window == window:
      return
    self.current_window = window
    click_event_func(event, window)

  def create_menu_item(self, parent, text, image, window, click_event_func):
    """Create Button as menu item"""
    img = CTkImage(dark_image=Image.open(get_image_path(image)), size=(25, 25))
    btn = CTkButton(parent, image=img, width=200, height=40, text=text, compound='left', anchor="w",
                    corner_radius=0, border_spacing=10, fg_color="transparent",
                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),)
    btn.bind("<Button-1>", lambda e: self.mouse_click(e, window, click_event_func))
    return btn
