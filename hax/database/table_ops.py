"""Database operation related to the setting"""
from dataclasses import dataclass
from enum import Enum

from classes.enums import Table
from database.db import DB
from exceptions.database import SQLException

db = DB()


@dataclass
class Criteria:
  """WHERE clousre criteria parameters"""
  class Op(Enum):
    """Different criteria operations in the SQL query"""
    EQ = "="
    GT = ">"
    GE = ">="
    LT = "<"
    LE = "<="
    LIKE = "LIKE"

  name: str
  value: str
  ops: Op = Op.EQ


def run(command: str, args: tuple = ()):
  """run SQL command and return result"""
  if command.lower().strip().startswith("select"):
    result = db.fetch(command, args)
  else:
    result = db.run(command, args)
    if not result:
      raise SQLException(f"Failed execuation SQL command [{command}]")
  return result


def select_all(table: Table):
  """Select all records from a table"""
  command = f"SELECT * FROM {Table(table).name}"  # noqa: S608
  return run(command)


def select_item(table: Table, criteria: list[Criteria]):
  """Select record from a table using criteria"""
  args: tuple = ()
  conditions = []
  for item in criteria:
    args += (item.value,)
    conditions.append(f"{item.name}{item.ops.value}?")
  condition = ",".join(conditions)
  command = f"SELECT * FROM {Table(table).name} WHERE {condition}"  # noqa: S608
  result = run(command, args)
  if len(result) > 1:
    raise SQLException(command)
  return result[0] if result else None
