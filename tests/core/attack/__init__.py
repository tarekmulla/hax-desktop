"""Basic classes to test attacks"""


class FakeResponse():
  def __init__(self, content: bytes):
    self.content = content

class FakeFrame:
  def __init__(self):
    self.success = 0
    self.fail = 0

  def get_result(self, result, is_success):
    if is_success:
      self.success = self.success + 1
    else:
      self.fail = self.fail + 1
