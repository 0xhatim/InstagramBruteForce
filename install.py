import os

install = ["colorama","termcolor","requests"]
for i in install:
    msg = "pip install "+ i
    os.system(msg)
