from cx_Freeze import setup, Executable

base = None

executables = [Executable("timeleft.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Tiempo restante",
    options = options,
    version = "1.01",
    description = 'Para contar las horas',
    executables = executables
)