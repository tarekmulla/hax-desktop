""""The application configuration singleton class"""
from enum import Enum
from os.path import dirname, exists

from classes.enums import Color
from exceptions.application import ConfigException
from yaml import safe_load


class AppConfig:
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
    raise FileNotFoundError(f"Application {config_type.value} config file not found in path: {file_path}")

  def get_app_initial_size(self):
    """get the application initial dimension"""
    if hasattr(self, "design") and "size" in self.design:
      return self.design["size"]
    raise ConfigException("size")

  def get_icon(self):
    """get the logo image path"""
    if hasattr(self, "design") and "images" in self.design and "icon" in self.design['images']:
      return f"{self.base_dir}/{self.design['images']['icon']}"
    raise ConfigException("icon")

  def get_logo(self):
    """get the logo image path"""
    if hasattr(self, "design") and "images" in self.design and "logo" in self.design['images']:
      return f"{self.base_dir}/{self.design['images']['logo']}"
    raise ConfigException("logo")

  def get_images_path(self):
    """get all images path"""
    if hasattr(self, "design") and "images" in self.design and "path" in self.design['images']:
      return f"{self.base_dir}/{self.design['images']['path']}"
    raise ConfigException("logo")

  def get_image_path(self, image_name):
    """get specific image path"""
    if image_name:
      image_path = f"{self.get_images_path()}/{image_name}"
      if exists(image_path):
        return image_path
      raise FileNotFoundError(f"Couldn't find image {image_name} in path {self.get_images_path()}")
    raise ValueError("Image name is not valid!")

  def get_color(self, color: Color):
    """Get the color code"""
    color_name = Color(color).name.lower()
    if hasattr(self, "design") and "colors" in self.design and color_name in self.design['colors']:
      return self.design["colors"][color_name]
    raise ConfigException(color)
