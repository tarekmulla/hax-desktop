"""The entry point to the application"""
from sys import path

from app import App
from utilities.config import BASE_DIR
from utilities.db.base import init_db
from utilities.log import init_log

if __name__ == "__main__":
  # import the root of the package
  path.append(BASE_DIR)

  init_log()
  init_db()

  app = App()
  app.run()
