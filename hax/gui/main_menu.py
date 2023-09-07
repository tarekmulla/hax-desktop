"""The main menu of the application"""
from tkinter import Frame, Label

from classes.enums import Color, Windows
from PIL import Image, ImageTk
from utilities.config import get_color, get_image_path


class MainMenu(Frame):
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
    super().__init__(master, bg=get_color(Color.SECONDARY))
    self.current_window = Windows.NONE
    self.current_item = Label()

  def init_items(self, event_func):
    """Initialize the menu items"""
    self.menu_items = [
      MainMenu.MenuItem("XSS Attack", "xss.png", Windows.XSS),
      MainMenu.MenuItem("SQLi Attack", "sqli.png", Windows.SQLI),
      MainMenu.MenuItem(),
      MainMenu.MenuItem(),
      MainMenu.MenuItem(),
      MainMenu.MenuItem("Setting", "setting.png", Windows.SETTING),
      MainMenu.MenuItem("About HaX", "about.png", Windows.ABOUT)
    ]

    for item in self.menu_items:
      btn_frame = Frame(self, bg=get_color(Color.SECONDARY))
      btn_frame.grid(column=0)
      self.create_menu_item(btn_frame, f"{' '*5}{item.name}", item.image,
                            item.window, event_func).grid()

  def mouse_hover(self, event):
    """Call when a mouse hover on menu item"""
    if self.current_item is not event.widget:
      event.widget["bg"] = get_color(Color.HOVER)

  def mouse_leave(self, event):
    """Call when a mouse leave the menu item"""
    if self.current_item is not event.widget:
      event.widget["bg"] = get_color(Color.SECONDARY)

  def mouse_click(self, event, window: Windows, click_event_func):
    """Call when a mouse click the menu item"""
    if self.current_window == window:
      return
    self.current_window = window
    if self.current_item:
      self.current_item["bg"] = get_color(Color.SECONDARY)  # type: ignore[attr-defined]
    self.current_item = event.widget
    self.current_item["bg"] = get_color(Color.HOVER)  # type: ignore[attr-defined]
    click_event_func(event, window)

  def create_menu_item(self, parent, text, image, window, click_event_func):
    """Create Button label"""
    if image and text:
      img = ImageTk.PhotoImage((Image.open(get_image_path(image))).resize((30, 30)))
      btn_lbl = Label(parent, width=200, height=50, text=text, image=img, compound='left',
                      bg=get_color(Color.SECONDARY),
                      foreground=get_color(Color.FORTH),
                      anchor="w", cursor="hand2")
      btn_lbl.image = img
      btn_lbl.bind("<Button-1>", lambda e: self.mouse_click(e, window, click_event_func))
      btn_lbl.bind("<Enter>", self.mouse_hover)
      btn_lbl.bind("<Leave>", self.mouse_leave)
    else:
      btn_lbl = Label(parent, height=3, bg=get_color(Color.SECONDARY))
    return btn_lbl
