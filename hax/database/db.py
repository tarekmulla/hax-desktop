""""Database operations"""
from sqlite3 import DatabaseError, IntegrityError, connect

from exceptions.database import DBException
from utilities.config import AppConfig


class DB:
  """database operations"""

  def __new__(cls):
    if not hasattr(cls, "instance"):
      cls.instance = super(DB, cls).__new__(cls)
    return cls.instance

  def __init__(self):
    self.app_config = AppConfig()
    self.__create_tables__()

  def __create_tables__(self):
    """Create tables"""
    self.run(self.app_config.db["attack"], None)
    self.run(self.app_config.db["setting"], None)

  def _execuate(self, command: str, args, with_commit: bool = False):
    """Execuate SQL command"""
    try:
      with connect(self.app_config.get_db_path()) as con:
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

  def run(self, command: str, args: tuple) -> bool:
    """Execuate non-select database command"""
    is_succ = False
    try:
      cur = self._execuate(command, args, True)
      is_succ = cur.rowcount > 0
      cur.close()
    except DBException:
      is_succ = False
    return is_succ

  def fetch(self, command: str, args: tuple) -> list:
    """Execuate select database command"""
    try:
      cur = self._execuate(command, args)
      result: list = cur.fetchall()
      cur.close()
      return result
    except DBException:
      return []
