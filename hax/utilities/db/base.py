""""Database base operations"""
from dataclasses import dataclass
from enum import Enum
from sqlite3 import DatabaseError, IntegrityError, connect

from classes.exception.database import DBException
from utilities.config import DB, get_db_path


def execuate(command: str, args, with_commit: bool = False):
  """Execuate SQL command"""
  try:
    with connect(get_db_path()) as con:
      cur = con.cursor()
      if args:
        cur.execute(command, args)
      else:
        cur.execute(command)
      if with_commit:
        con.commit()
    return cur
  except IntegrityError as ex:
    raise DBException(f"Can not insert [{args}] twice", ex.args) from ex
  except DatabaseError as ex:
    raise DBException(f"Database error while execuating command [{command}] with args: [{args}]", ex.args) from ex
  except Exception as ex:
    raise DBException(f"Failed execuating command [{command}] with args: [{args}]", ex.args) from ex


def run(command: str, args: tuple) -> bool:
  """Execuate non-select database command"""
  is_succ = False
  try:
    cur = execuate(command, args, True)
    is_succ = cur.rowcount > 0
    cur.close()
  except DBException:
    is_succ = False
  return is_succ


def fetch(command: str, args: tuple) -> list:
  """Execuate select database command"""
  try:
    cur = execuate(command, args)
    result: list = cur.fetchall()
    cur.close()
    return result
  except DBException:
    return []


def init_db():
  """Initilaize database tables"""
  run(DB["attack"], None)
  run(DB["setting"], None)


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
