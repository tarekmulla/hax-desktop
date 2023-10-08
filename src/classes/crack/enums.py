"""All enums in the app"""
from enum import Enum


class CrackType(Enum):
  """All attack types"""
  RAINBOW = 1
  BRUTE_FORCE = 2

  @classmethod
  def get_names(cls):
    """Get all enum names"""
    # pylint: disable=W0212,E1101
    return CrackType._member_names_


class HashAlgorithm(Enum):
  """Supported hash algorithms"""
  MD5 = 1
  SHA265 = 2
  BCRYPT = 3

  @classmethod
  def get_names(cls):
    """Get all enum names"""
    # pylint: disable=W0212,E1101
    return CrackType._member_names_
