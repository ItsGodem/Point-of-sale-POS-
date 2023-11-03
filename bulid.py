from cx_Freeze import setup, Executable

executables = [Executable("main.py")]  #file name here
setup(
    name="MyApp",
    version="1.0",
    description="My Python application",
    executables=executables
)