"""This hook should collect all binary files and any hidden modules that array_sum_example needs

Our (some-what inadequate) docs for writing PyInstaller hooks are kept here:
https://pyinstaller.readthedocs.io/en/stable/hooks.html

"""
from PyInstaller.utils.hooks import collect_dynamic_libs, is_module_satisfies

# Collect all DLLs inside array_sum_examples's installation folder, dump them into built
# app's root.
binaries = collect_dynamic_libs("array_sum_example")

# If using Conda without any non-conda virtual environment manager:

# Submodules PyInstaller cannot detect (probably because they are only imported
# by extension modules, which PyInstaller cannot read).
# hiddenimports = ['numpy.core._dtype_ctypes']
# if is_conda:
#     hiddenimports.append("six")

# Remove testing and building code and packages that are referenced throughout
# NumPy but are not really dependencies.
# excludedimports = [
#     "scipy",
#     "pytest",
#     "nose",
#     "f2py",
#     "setuptools",
#     "numpy.f2py",
#     "distutils",
#     "numpy.distutils",
# ]
