"""CrossSite Scripting injection frame"""
# pylint: disable=R0801
from tkinter import END, INSERT

from customtkinter import CTk

from classes.crack.brute_force import BruteForce
from classes.crack.crack_pass_manager import CrackPassManager
from classes.crack.enums import CrackType, HashAlgorithm
from classes.crack.password_rule import PasswordRule
from classes.crack.rainbow import Rainbow
from gui.frames.base_frame import BaseFrame


class CrackPasswordFrame(BaseFrame):
  """Crack password frame"""

  def __init__(self, master: CTk):
    super().__init__(master, "Crack Password")
    self.crack_manager = CrackPassManager()

  def __init_frame__(self):
    """Initialize frame components"""
    super().__init_frame__()

    self.grid_columnconfigure((0, 2), weight=1)
    self.grid_columnconfigure((1, 3), weight=2)
    self.grid_rowconfigure(9, weight=1)

    self.add_label("Hash password").grid(row=0, column=0)
    self.hash_password = self.add_entry()
    self.hash_password.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="ew", columnspan=3)

    self.add_label("Crack Type").grid(row=1, column=0)
    self.opt_crack_type = self.add_option("Crack Type", *(CrackType.get_names()))
    self.opt_crack_type.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="w", columnspan=3)

    self.add_label("Wordlist file").grid(row=2, column=0)
    self.wordlist_file = self.add_entry()
    self.wordlist_file.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="ew", columnspan=3)

    self.add_label("Character set").grid(row=3, column=0)
    self.character_set = self.add_entry()
    self.character_set.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="ew", columnspan=3)

    self.add_label("Minimum length").grid(row=4, column=0)
    self.min_length = self.add_num_entry()
    self.min_length.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

    self.add_label("Maximum length").grid(row=4, column=2)
    self.max_length = self.add_num_entry()
    self.max_length.grid(row=4, column=3, padx=(10, 10), pady=(10, 10), sticky="ew")

    self.add_label("Hash Algorithm").grid(row=5, column=0)
    self.opt_hash_algorithm = self.add_option("Hash Algorithm", *(HashAlgorithm.get_names()))
    self.opt_hash_algorithm.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

    self.add_label("Rainbow table length").grid(row=6, column=0)
    self.rainbow_length = self.add_num_entry()
    self.rainbow_length.grid(row=6, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

    self.add_label("Rainbow table depth").grid(row=6, column=2)
    self.rainbow_depth = self.add_num_entry()
    self.rainbow_depth.grid(row=6, column=3, padx=(10, 10), pady=(10, 10), sticky="ew")

    self.add_button("Crack Password", self.crack_password).grid(row=7, column=0, columnspan=4)

    self.progbar_crack = self.add_progressbar()
    self.progbar_crack.grid(row=8, column=0, columnspan=4, padx=(30, 30), pady=(10, 10), sticky="news")

    self.txt_log = self.add_log()
    self.txt_log.grid(row=9, column=0, columnspan=4, sticky="news")

  def set_default_input(self):
    """default value for the input"""
    super().set_default_input()
    self.hash_password.insert(INSERT, "c2368d3d45705a56e51ec5940e187f8d")
    self.wordlist_file.insert(INSERT, "wordlist.txt")
    self.character_set.insert(INSERT, "0-9")
    self.opt_crack_type.set(CrackType.RAINBOW.name)
    self.opt_hash_algorithm.set(HashAlgorithm.MD5.name)
    self.min_length.insert(INSERT, 4)
    self.max_length.insert(INSERT, 4)
    self.rainbow_length.insert(INSERT, 6000)
    self.rainbow_depth.insert(INSERT, 10)

  def crack_password(self):
    """prepare the crack and start the cracking the password"""
    hash_pass = self.hash_password.get()
    crack_method = CrackType[self.opt_crack_type.get()]

    if crack_method is CrackType.BRUTE_FORCE:
      wordlist_file = self.wordlist_file.get()
      crack = BruteForce(wordlist_file, [])
    elif crack_method is CrackType.RAINBOW:
      char_set = self.character_set.get()
      hash_algo = HashAlgorithm[self.opt_hash_algorithm.get()]
      min_pass_len = int(self.min_length.get())
      max_pass_len = int(self.max_length.get())
      rainbow_len = int(self.rainbow_length.get())
      rainbow_dep = int(self.rainbow_depth.get())
      rule = PasswordRule(char_set, min_pass_len, max_pass_len)
      crack = Rainbow(rule, rainbow_len, rainbow_dep, hash_algo)

    self.crack_num = 0
    self.crack_manager.start(crack, hash_pass, self.update_status)

  def update_status(self, total, index, message):
    """Update the form status"""
    self.progbar_crack.set((index / total) if total else 0)
    if message:
      self.txt_log.insert(END, message + "\n")
