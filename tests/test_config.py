"""Unit tests for the config class"""


import pytest

from classes.gui.enums import Color
from utilities.config import get_app_initial_size, get_color, get_icon, get_image_path


@pytest.mark.parametrize("image", [("about.png"), ("icon.png"), ("logo.png"), ("setting.png"), ("sqli.png"), ("xss.png")])
def test_get_required_images(image):
  assert get_image_path(image)

@pytest.mark.parametrize("image", [("notexist.png")])
def test_get_not_exist_images(image):
  with pytest.raises(FileNotFoundError):
    get_image_path(image)

@pytest.mark.parametrize("color", [(Color.PRIMARY), (Color.SECONDARY), (Color.THIRD), (Color.FORTH), (Color.BORDER), (Color.HOVER)])
def test_get_colors(color):
  assert get_color(color)

def test_get_icon():
  assert get_icon()

def test_get_app_initial_size():
  assert get_app_initial_size()
