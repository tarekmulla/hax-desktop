"""Unit tests for the database operations"""

import pytest

from core.classes.exception.database import SQLException
from core.utilities.db.tbl_setting import get_all_setting, get_setting_by_name, update_setting

from . import FakeCursor


def test_insert_setting(mocker):
  mocker.patch('core.utilities.db.base.execuate', return_value=FakeCursor(1))
  mocker.patch('core.utilities.db.tbl_setting.get_setting_by_name', return_value=None)
  assert update_setting("setting_name", "setting_val") == True


def test_update_setting(mocker):
  mocker.patch('core.utilities.db.base.execuate', return_value=FakeCursor(1))
  mocker.patch('core.utilities.db.tbl_setting.get_setting_by_name', return_value=[0])
  assert update_setting("setting_name", "setting_val") == True


def test_get_setting_by_name(mocker):
  mocker.patch('core.utilities.db.base.execuate', return_value=FakeCursor(1, ["TEST"]))
  assert get_setting_by_name("setting_name") == "TEST"


def test_get_setting_by_name_failure(mocker):
  with pytest.raises(SQLException):
    mocker.patch('core.utilities.db.base.execuate', return_value=FakeCursor(2, ["TEST1", "TEST2"]))
    assert get_setting_by_name("setting_name")


def test_get_all_setting(mocker):
  mocker.patch('core.utilities.db.base.execuate', return_value=FakeCursor(2, [[0,"name0","value0"], [1,"name1","value1"]]))
  assert len(get_all_setting()) == 2
