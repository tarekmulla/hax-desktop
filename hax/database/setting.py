"""Database operation related to the setting"""
from classes.enums import Table
from database.table_operation import run, select_all


def update_setting(name: str, value: str):
  """insert setting into database"""
  item = get_setting_by_name(name)
  if item:
    command = "UPDATE setting SET name = ?, value = ? WHERE id = ?"
    item_id = item[0]
    args = (name, value, item_id,)
  else:
    command = "INSERT INTO setting (name, value) values (?, ?)"
    args = (name, value,)

  return run(command, args)


def get_setting_by_name(name: str):
  """get setting value from database"""
  command = "SELECT * from setting WHERE name = ?"
  args = (name,)
  result = run(command, args)
  return result[0] if result else None


def get_all_setting():
  """get setting value from database"""
  result = select_all(Table.SETTING)
  setting = {}
  for item in result:
    setting[item[1]] = item[2]
  return setting
