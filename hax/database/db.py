""""Database operations"""
from sqlite3 import Connection, connect


class DB(object):
  """database operations"""

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(DB, cls).__new__(cls)
    return cls.instance

  def __init__(self):
    self.con: Connection = connect("hax.db")
    self.__create_tables__()

  def __create_tables__(self):
    """Create tables"""
    cur = self.con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS attack( \
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                url TEXT NOT NULL, \
                parameters TEXT NOT NULL \
                )")
    cur.execute("CREATE TABLE IF NOT EXISTS setting( \
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                name TEXT NOT NULL, \
                value TEXT NOT NULL \
                )")

  def run(self, command: str, args: tuple) -> bool:
    """Execuate non-select database command"""
    is_succ = False
    try:
      cur = self.con.cursor()
      if args:
        cur.execute(command, args)
      else:
        cur.execute(command)
      self.con.commit()
      is_succ = cur.rowcount > 0
      cur.close()
    except Exception:
      is_succ = False
    return is_succ

  def fetch(self, command: str, args: tuple) -> list:
    """Execuate select database command"""
    try:
      cur = self.con.cursor()
      if args:
        cur.execute(command, args)
      else:
        cur.execute(command)
      result = cur.fetchall()
      cur.close()
      return result
    except Exception:
      return None
