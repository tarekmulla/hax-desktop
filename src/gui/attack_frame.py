"""base class for all attacks"""
from os.path import join
from tkinter import END

from classes.attacks.attack import Attack
from gui.base_frame import BaseFrame
from utilities.attack import load_payloads, summarize_response
from utilities.config import BASE_DIR


class AttackFrame(BaseFrame):
  """base class for the attack forms"""

  attack_num = 0

  def __init__(self, master, title: str, payloads_file: str):
    super().__init__(master=master, title=title)
    self.attack = None
    self.payloads_path = join(BASE_DIR, ".payloads", payloads_file)

  def __init_frame__(self):
    """Initialize frame components"""
    super().__init_frame__()
    self.progbar_attacks = self.add_progressbar(500)
    self.txt_log = self.add_log(7, 0, 2, 12)

  def set_default_input(self):
    """default value for the input"""
    # configuring the log tags to colorize output
    super().set_default_input()
    self.txt_log.tag_config("SUCCESS", background="green")
    self.txt_log.tag_config("FAILED", background="red")

  def destroy(self) -> None:
    if self.attack:
      self.attack.stop_attack()
    super().destroy()

  def start_attack(self, placeholder_text: str):
    """Start the attack"""
    if not self.attack:
      return
    self.txt_log.delete(1.0, END)  # clear text
    self.attack_num = 0
    self.payloads: list = load_payloads(placeholder_text, self.payloads_path)
    self.attack.start(self.payloads, self.add_result)

  def add_result(self, payload: str, attack: Attack):
    """Add result to the log text component"""
    result = summarize_response(payload, attack)
    self.txt_log.insert(END, result)
    row = (self.attack_num * 7) + 5
    # add tag using indices for the part of text to be highlighted
    self.txt_log.tag_add("SUCCESS" if attack.is_success else "FAILED", f"{row}.0", f"{row}.100")
    self.txt_log.see(END)
    self.progbar_attacks.step(99.9 * (1 / len(self.payloads)))
    self.attack_num += 1
