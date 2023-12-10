"""Import the application package"""
from os import environ, system
from os.path import dirname, realpath
from sys import path

from customtkinter import CTk

# import the root of the package
hax_path = f"{dirname(realpath(__file__))}/.."
path.append(hax_path)

TEST_DIR = dirname(__file__)

environ['DISPLAY']=':1.0'
system('Xvfb :1 -screen 0 1600x1200x16  &')

class FakeWindow(CTk):
  """Fake window to test GUI"""
