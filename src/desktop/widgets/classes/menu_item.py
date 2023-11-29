"""Class represent menu item"""
from core.classes.gui.enums import Windows


class MenuItem:
  """Class represent one menu item in the app"""
  # pylint: disable=too-few-public-methods
  def __init__(self, name="", image="", window=Windows.NONE):
    self.name = name
    self.image = image
    self.window = window
