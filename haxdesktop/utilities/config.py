""""load all application configuration files (YAML format)"""
from os.path import dirname, exists, join

from haxcore.exception.application import ConfigException
from yaml import safe_load

from haxdesktop.classes.enums import Color, ConfigType

ROOT_DIR = dirname(dirname(__file__))


def load_config(config_type) -> dict:
  """Load specific configuration file"""
  file_path = join(ROOT_DIR, "assets", config_type.value)
  if exists(file_path):
    with open(file_path, encoding="UTF-8") as config:
      data: dict = safe_load(config)
      return data
  raise FileNotFoundError(f"Application {config_type.value} config file not found in path: {file_path}")


DESIGN = load_config(ConfigType.DESIGN)
GENERAL = load_config(ConfigType.GENERAL)


def get_app_initial_size():
  """get the application initial size"""
  if "size" in DESIGN:
    return DESIGN["size"]
  raise ConfigException("size")


def get_app_min_size():
  """get the application min size"""
  if "min_size" in DESIGN:
    return DESIGN["min_size"]
  raise ConfigException("min_size")


def get_icon():
  """get the logo image path"""
  if "images" in DESIGN and "icon" in DESIGN['images']:
    return f"{ROOT_DIR}/{DESIGN['images']['icon']}"
  raise ConfigException("icon")


def get_logo():
  """get the logo image path"""
  if "images" in DESIGN and "logo" in DESIGN['images']:
    return f"{ROOT_DIR}/{DESIGN['images']['logo']}"
  raise ConfigException("logo")


def get_images_path():
  """get all images path"""
  if "images" in DESIGN and "path" in DESIGN['images']:
    return f"{ROOT_DIR}/{DESIGN['images']['path']}"
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
