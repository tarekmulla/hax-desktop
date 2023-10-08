"""The main menu of the application"""
from customtkinter import CTkButton, CTkFont, CTkFrame, CTkImage, CTkLabel
from PIL import Image

from classes.gui.enums import Windows
from utilities.config import get_icon, get_image_path


class MainMenu(CTkFrame):
  """The main menu of the application"""
  class MenuItem:
    """Class represent one menu item in the app"""
    # pylint: disable=too-few-public-methods
    def __init__(self, name="", image="", window=Windows.NONE):
      self.name = name
      self.image = image
      self.window = window

  def __init__(self, master):
    self.master = master
    super().__init__(master, width=150, corner_radius=0)
    self.current_window = Windows.NONE

  def init_items(self, event_func):
    """Initialize the menu items"""
    self.menu_items_top = [
      MainMenu.MenuItem("XSS Attack", "xss.png", Windows.XSS),
      MainMenu.MenuItem("SQLi Attack", "sqli.png", Windows.SQLI),
      MainMenu.MenuItem("Crack Password", "password.png", Windows.CRACK_PASS),
    ]
    self.menu_items_down = [
      MainMenu.MenuItem("Setting", "setting.png", Windows.SETTING),
      MainMenu.MenuItem("About HaX", "about.png", Windows.ABOUT)
    ]
    self.grid_rowconfigure(len(self.menu_items_top)+1, weight=1)

    logo = CTkImage(dark_image=Image.open(get_icon()), size=(40, 40))
    lbl_logo = CTkLabel(self, text=" HaX Tool", image=logo, compound="left", font=CTkFont(size=20, weight="bold"))
    lbl_logo.grid(row=0, column=0, padx=0, pady=10, sticky="ew")
    row = 1
    for item in self.menu_items_top:
      btn = self.create_menu_item(self, item.name, item.image, item.window, event_func)
      btn.grid(row=row, column=0, sticky="nsew")
      row = row + 1
    row = row + 1
    for item in self.menu_items_down:
      btn = self.create_menu_item(self, item.name, item.image, item.window, event_func)
      btn.grid(row=row, column=0, sticky="nsew")
      row = row + 1

  def mouse_click(self, event, window: Windows, click_event_func):
    """Call when a mouse click the menu item"""
    is_window = window in (Windows.ABOUT, Windows.SETTING)
    if not is_window:
      if self.current_window == window:
        return
      self.current_window = window
    click_event_func(event, window, is_window)

  def create_menu_item(self, parent, text, image, window, click_event_func):
    """Create Button as menu item"""
    img = CTkImage(dark_image=Image.open(get_image_path(image)), size=(25, 25))
    btn = CTkButton(parent, image=img, width=200, height=40, text=text, compound='left', anchor="w",
                    corner_radius=0, border_spacing=10, fg_color="transparent",
                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),)
    btn.bind("<Button-1>", lambda e: self.mouse_click(e, window, click_event_func))
    return btn
