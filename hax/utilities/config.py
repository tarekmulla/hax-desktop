""""load all application configuration files (YAML format)"""
from os.path import dirname, exists

from classes.enums import Color, ConfigType
from classes.exception.application import ConfigException
from yaml import safe_load

BASE_DIR = dirname(dirname(__file__))


def load_config(config_type) -> dict:
  """Load specific configuration file"""
  file_path = f"{BASE_DIR}/.config/{config_type.value}"
  if exists(file_path):
    with open(file_path, encoding="UTF-8") as config:
      data: dict = safe_load(config)
      return data
  raise FileNotFoundError(f"Application {config_type.value} config file not found in path: {file_path}")


DESIGN = load_config(ConfigType.DESIGN)
GENERAL = load_config(ConfigType.GENERAL)
DB = load_config(ConfigType.DB)  # pylint: disable=invalid-name
LOG = load_config(ConfigType.LOG)


def get_db_path():
  """get the application database path"""
  if "name" in DB:
    return f"{BASE_DIR}/{DB['name']}"
  raise ConfigException("db")


def get_app_initial_size():
  """get the application initial dimension"""
  if "size" in DESIGN:
    return DESIGN["size"]
  raise ConfigException("size")


def get_icon():
  """get the logo image path"""
  if "images" in DESIGN and "icon" in DESIGN['images']:
    return f"{BASE_DIR}/{DESIGN['images']['icon']}"
  raise ConfigException("icon")


def get_logo():
  """get the logo image path"""
  if "images" in DESIGN and "logo" in DESIGN['images']:
    return f"{BASE_DIR}/{DESIGN['images']['logo']}"
  raise ConfigException("logo")


def get_images_path():
  """get all images path"""
  if "images" in DESIGN and "path" in DESIGN['images']:
    return f"{BASE_DIR}/{DESIGN['images']['path']}"
  raise ConfigException("logo")


def get_image_path(image_name):
  """get specific image path"""
  if image_name:
    image_path = f"{get_images_path()}/{image_name}"
    if exists(image_path):
      return image_path
    raise FileNotFoundError(f"Couldn't find image {image_name} in path {get_images_path()}")
  raise ValueError("Image name is not valid!")


def get_color(color: Color):
  """Get the color code"""
  color_name = Color(color).name.lower()
  if "colors" in DESIGN and color_name in DESIGN['colors']:
    return DESIGN["colors"][color_name]
  raise ConfigException(color_name)
