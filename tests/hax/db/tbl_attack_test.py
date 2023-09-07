"""Unit tests for the database operations"""

import pytest
from classes.enums import AttackType, RequestType
from classes.exception.database import SQLException
from utilities.db.tbl_attack import get_all_attacks, get_attack_by_url, insert_attack, update_attack

from . import FakeCursor


def test_insert_attack(mocker):
  mocker.patch('utilities.db.base.execuate', return_value=FakeCursor(1))
  assert insert_attack("attack_url", RequestType.GET, AttackType.XSS, "attack_params") == True


def test_update_attack(mocker):
  mocker.patch('utilities.db.base.execuate', return_value=FakeCursor(1))
  assert update_attack(0, "attack_url", RequestType.GET, AttackType.XSS, "attack_params") == True


def test_get_attack_by_url(mocker):
  mocker.patch('utilities.db.base.execuate', return_value=FakeCursor(1, ["TEST"]))
  assert get_attack_by_url("attack_url") == "TEST"


def test_get_attack_by_url_failure(mocker):
  with pytest.raises(SQLException):
    mocker.patch('utilities.db.base.execuate', return_value=FakeCursor(2, ["TEST1", "TEST2"]))
    assert get_attack_by_url("attack_url")


def test_get_all_attacks(mocker):
  mocker.patch('utilities.db.base.execuate', return_value=FakeCursor(2, [
    [0,"",RequestType.GET,"",AttackType.XSS],
    [2,"",RequestType.GET,"",AttackType.XSS]])
  )
  assert len(get_all_attacks()) == 2
