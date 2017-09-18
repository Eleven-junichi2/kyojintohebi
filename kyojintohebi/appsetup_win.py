import sys
from cx_Freeze  import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

setup(  name = "Kyojintohebi",
        version = "0.5",
        description = "kyojintohebi",
        author = "Junichi Suetsugu",
        executables = [Executable("game.py", copyright="Junichi Suetsugu")])
