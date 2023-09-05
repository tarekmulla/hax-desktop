""""The application configuration singleton class"""
from enum import Enum
from os.path import dirname, exists

from classes.enums import Color
from yaml import safe_load


class AppConfig(dict):
  """The application configuration singleton class"""

  class Type(Enum):
    """Different confiuration files"""
    DESIGN = "design.yml"
    GENERAL = "general.yml"

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(AppConfig, cls).__new__(cls)
    return cls.instance

  def __init__(self):
    self._load_all()

  def _load_all(self):
    """load all application configuration files (YAML format)"""
    self.base_dir = dirname(__file__)
    self.design = self._load_config(AppConfig.Type.DESIGN)
    self.general = self._load_config(AppConfig.Type.GENERAL)

  def _load_config(self, config_type):
    """Load specific configuration file"""
    file_path = f"{self.base_dir}/{config_type.value}"
    if exists(file_path):
      with open(file_path, encoding="UTF-8") as config:
        return safe_load(config)
    else:
      raise FileNotFoundError(f"Application {config_type.value} config file not found in path: {file_path}")

  def get_app_initial_size(self):
    """get the application initial dimension"""
    return self.design["size"]

  def get_icon(self):
    """get the logo image path"""
    return f"{self.base_dir}/{self.design['images']['icon']}"

  def get_logo(self):
    """get the logo image path"""
    return f"{self.base_dir}/{self.design['images']['logo']}"

  def get_images_path(self):
    """get all images path"""
    return f"{self.base_dir}/{self.design['images']['path']}"

  def get_image_path(self, image_name):
    """get specific image path"""
    return f"{self.get_images_path()}/{image_name}"

  def get_color(self, color: Color):
    """Get the color code"""
    color_name = Color(color).name.lower()
    return self.design["colors"][color_name]
