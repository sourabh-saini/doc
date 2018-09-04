application_title = "Weather Forecast App"
main_python_file = "Weather_forcasting.py"

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform =="win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
        name = application_title,
        version = "0.1",
        description = "Simple test",
        options = {"build_exe" : {"includes" : includes}},
        executables = [Executable(main_python_file,base = base)]

)