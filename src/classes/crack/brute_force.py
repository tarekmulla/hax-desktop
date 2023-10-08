"""Perform password cracking using brute-force"""
from classes.crack.crack_base import CrackBase
from classes.crack.enums import CrackType
from utilities.wordlist import load_wordlist


class BruteForce(CrackBase):
  """Class to perform brute force password cracking"""
  def __init__(self, wordlist_file: str, rules: list):
    super().__init__(CrackType.BRUTE_FORCE)
    self.wordlist: list = load_wordlist(wordlist_file, rules)
