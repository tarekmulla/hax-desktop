from os import environ, system

environ['DISPLAY']=':1.0'
system('Xvfb :1 -screen 0 1600x1200x16  &')
