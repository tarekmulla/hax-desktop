"""Database operation related to the setting"""
from classes.enums import Table
from database.db import DB
from exceptions.database import SQLException

db = DB()


def run(command: str, args: tuple = None):
  """run SQL command"""
  if "select" in command.lower():
    result = db.fetch(command, args)
    return result
  else:
    result = db.run(command, args)
    if not result:
      raise SQLException("Failed execuation command")
    else:
      return True


def select_all(table: Table):
  """Select all records from a table"""
  command = f"SELECT * FROM {Table(table).name}"  # noqa: S608
  return run(command)
