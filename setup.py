from cx_Freeze import setup, Executable

# Opsi Build
buildOptions = dict(
    packages=['termcolor', 
              'cryptography'
              ],  # Sertakan library eksternal di sini
    includes=[],
    include_files=[
        'menu.py',
        'login_data.py',
        'check.py',  # File tambahan yang mungkin dibutuhkan
    ],
    excludes=[]
)

# Tentukan skrip utama aplikasi Anda
base = None  # Gunakan None untuk aplikasi konsol di Linux

executables = [
    Executable('main.py', base=base)
]

setup(
    name='SYMPLE_OS_WITH_PYTHON',
    version='1.0',
    description='My Project Os With Python3',
    options={'build_exe': buildOptions},
    executables=executables
)
