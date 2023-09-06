"""Unit tests for the config class"""


import pytest
from utilities.config import AppConfig
from classes.enums import Color

@pytest.fixture
def app_config() -> AppConfig:
  """Return an AppConfig instance"""
  return AppConfig()

@pytest.mark.parametrize("config", [("design"), ("general")])
def test_load_config_files(app_config, config):
  """Test loading default configuration is success"""
  assert hasattr(app_config, config)

@pytest.mark.parametrize("image", [("about.png"), ("icon.png"), ("logo.png"), ("setting.png"), ("sqli.png"), ("xss.png")])
def test_get_required_images(app_config, image):
  assert app_config.get_image_path(image)

@pytest.mark.parametrize("image", [("notexist.png")])
def test_get_not_exist_images(app_config, image):
  with pytest.raises(FileNotFoundError):
    app_config.get_image_path(image)

@pytest.mark.parametrize("color", [(Color.PRIMARY), (Color.SECONDARY), (Color.THIRD), (Color.FORTH), (Color.BORDER), (Color.HOVER)])
def test_get_colors(app_config, color):
  assert app_config.get_color(color)

def test_get_icon(app_config):
  assert app_config.get_icon()

def test_get_app_initial_size(app_config):
  assert app_config.get_app_initial_size()
