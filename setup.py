from cx_Freeze import setup, Executable

# Build
buildOptions = dict(
    packages=['termcolor', 
              'cryptography'
              ], 
    includes=[],
    include_files=[
        'menu.py',
        'login_data.py',
        'check.py',  
    ],
    excludes=[]
)

base = None  # None untuk aplikasi konsol di Linux

# Skrip utama aplikasi Anda
executables = [
    Executable('main.py', base=base)
]

setup(
    name='PROJECT-2-PYTHON',
    version='1.0',
    description='Terminal Project With Python3',
    options={'build_exe': buildOptions},
    executables=executables
)
