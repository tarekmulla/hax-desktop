"""Database operation related to the attacks"""
from classes.attack import Attack
from database.table_operation import run


def add_attack(attack: Attack):
  """Insert attack into database"""
  command = "INSERT INTO attack (url, parameters) values (?, ?)"
  args = (attack.url, attack.paramaters)
  return run(command, args)
