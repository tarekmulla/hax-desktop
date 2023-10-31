"""Perform password cracking using brute-force"""
from hashlib import md5, sha256
from itertools import product
from os import makedirs, remove
from os.path import dirname, exists, join
from shlex import split
from subprocess import PIPE, Popen

import bcrypt

from classes.crack.crack_base import CrackBase
from classes.crack.enums import CrackType, HashAlgorithm
from classes.crack.wordlist_rules import WordlistRules
from utilities.config import BASE_DIR
from utilities.wordlist import load_wordlist


class BruteForce(CrackBase):
  """Class to perform brute force password cracking"""
  def __init__(self, wordlist_file: str, wordlist_rules: WordlistRules):
    super().__init__(CrackType.BRUTE_FORCE)
    self.wordlist_file = join(BASE_DIR, ".wordlist", wordlist_file)
    self.wordlist: list = load_wordlist(self.wordlist_file, wordlist_rules)
    self.wordlist_rules = wordlist_rules

  def _generate_password_file(self, hash_pass):
    file_name = "crack.pass"
    file_path = join(BASE_DIR, ".brute_force", file_name)
    if not exists(dirname(file_path)):
      makedirs(dirname(file_path))
    with open(file_path, "w", encoding="UTF-8") as file:
      file.write(hash_pass)
    return file_path

  def get_all_rules(self, charset, count):
    """Rainbow table generation method"""
    rules_list = []
    perm = list(product(charset, repeat=count))
    rules_list = [(''.join(p).replace('', ' $'))[1:-2] for p in perm]
    return rules_list

  def _generate_rules_file(self, wordlist_rules: WordlistRules):
    file_name = "crack.rules"
    file_path = join(BASE_DIR, ".brute_force", file_name)
    if not exists(dirname(file_path)):
      makedirs(dirname(file_path))
    with open(file_path, "w", encoding="UTF-8") as file:
      if wordlist_rules.postfix_count > 0:
        rules_list = self.get_all_rules(wordlist_rules.postfix_charset, wordlist_rules.postfix_count)
        for rule in rules_list:
          file.write(rule + "\n")
      if wordlist_rules.prefix_count > 0:
        rules_list = self.get_all_rules(wordlist_rules.prefix_charset, wordlist_rules.prefix_count)
        for rule in rules_list:
          file.write(rule + "\n")
    return file_path

  def start(self, hash_pass, hash_algorithm: HashAlgorithm, stop_flag, update_status_func):
    """Start brute-force password cracking process using hashcat"""
    password_file = self._generate_password_file(hash_pass)
    rules_file = self._generate_rules_file(self.wordlist_rules)
    try:
      algorithm_code = 0
      if hash_algorithm == HashAlgorithm.MD5:
        algorithm_code = 0
      elif hash_algorithm == HashAlgorithm.BCRYPT:
        algorithm_code = 3200
      elif hash_algorithm == HashAlgorithm.SHA256:
        algorithm_code = 1420

      command = f"hashcat -m {algorithm_code} '{password_file}' '{self.wordlist_file}' -r '{rules_file}'"
      args = split(command)
      pipe = Popen(args, stdout=PIPE)
      pipe.communicate()
      password_output = Popen(split(f"{command} --show"), stdout=PIPE).communicate()[0]
      if password_output:
        password_hash = password_output.decode().split(":")
        password = password_hash[1] if len(password_hash) == 2 else None
    except Exception as ex:
      password = None

    if password:
      update_status_func(0, 0, f"Password found, the password is: {password}")
    else:
      update_status_func(0, 0, "Password not found!")
    remove(password_file)
    remove(rules_file)

  def start2(self, hash_pass, hash_algorithm: HashAlgorithm, stop_flag, update_status_func):
    """Start brute-force password cracking process using hashcat"""
    password = self.find_hash(hash_pass, hash_algorithm)
    if password:
      update_status_func(0, 0, f"Password found, the password is: {password}")
    else:
      update_status_func(0, 0, "Password not found!")

  def find_hash(self, hash_pass, hash_algorithm: HashAlgorithm):
    """Find hash based on wordlist"""
    with open(self.wordlist_file, "r", encoding="UTF-8") as file:
      wordlist = file.readlines()
    hash_pass_hexdigest = hash_pass.encode()
    for word in wordlist:
      word_bytes = "grandmother".strip().encode()
      if hash_algorithm == HashAlgorithm.MD5:
        hash_result = md5(word_bytes)
        hash_hexdigest = hash_result.hexdigest()
      elif hash_algorithm == HashAlgorithm.SHA256:
        hash_result = sha256(word_bytes)
        hash_hexdigest = hash_result.hexdigest()
      elif hash_algorithm == HashAlgorithm.BCRYPT:
        salt = bcrypt.gensalt()
        hash_hexdigest = bcrypt.hashpw(word_bytes, salt)
      if hash_pass_hexdigest == hash_hexdigest:
        return word
