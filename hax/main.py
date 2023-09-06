"""The entry point to the application"""
from sys import path

from app import App
from utilities.config import AppConfig
from utilities.log import init_log

if __name__ == "__main__":
  app_config = AppConfig()
  # import the root of the package
  path.append(app_config.base_dir)

  # initilaize the log within the system
  init_log(app_config)

  app = App()
  app.run()
