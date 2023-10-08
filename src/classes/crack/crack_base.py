"""Base class to crack password"""
from classes.crack.enums import CrackType


class CrackBase:
  """Class represents Cyber Attack"""
  def __init__(self, crack_type: CrackType):
    self.crack_type = crack_type

  def start(self, hash_pass, stop_flag, update_status_func):
    """Start cracking process"""
    if not stop_flag():
      return False
    update_status_func()
    return hash_pass
