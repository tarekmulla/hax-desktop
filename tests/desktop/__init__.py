from os import environ, system

from customtkinter import CTk

environ['DISPLAY']=':1.0'
system('Xvfb :1 -screen 0 1600x1200x16  &')

class FakeWindow(CTk):
  """Fake window to test GUI"""
