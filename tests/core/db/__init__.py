"""Database functionalities test module"""
from sqlite3 import Connection

from .. import TEST_DIR


class TestConnection(Connection):
  """Create Test database"""
  def __init__(self):
    super().__init__(f"{TEST_DIR}/TEST.db")


class FakeCursor():
  """Fake sqlite cursor for testing"""
  def __init__(self, rowcount: int = 0, items = None):
    self.rowcount = rowcount
    self.items = items

  def close(self):
    """mock close method"""
    return None

  def fetchall(self):
    """mock fetchall method"""
    return self.items
