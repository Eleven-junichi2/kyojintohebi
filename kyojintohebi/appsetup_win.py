import sys
from cx_Freeze  import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

exe = Executable(script="game.py", base=base, copyright="Junichi Suetsugu")

setup(  name = "Kyojintohebi",
        version = "0.5",
        description = "kyojintohebi",
        author = "Junichi Suetsugu",
        options = {"build_exe": build_exe_options},
        executables = [exe])
