# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:06:13 2017

@author: Soumendra Kumar Sahoo
"""
from distutils.core import setup
from Cython.Build import cythonize
import py_compile
import os


# collect all py and __init__.py files
base_dir = os.getcwd()
init_py = "__init__.py"

py_files = []
pyc_files = ["stock_alert.py"]
for dir, subdir, files in os.walk(base_dir):
    rel_path = dir.split(base_dir)
    if len(rel_path) > 1:
        rel_path = rel_path[1].replace("\\", "/")
    else:
        rel_path = ""

    for filename in files:
        if filename == init_py:
            pyc_files.append((rel_path + "/" + init_py).lstrip("/"))
        elif filename[-3:] == ".py":
            if filename == pyc_files[0]:
                continue
            py_files.append((rel_path + "/" + filename).lstrip("/"))

py_compile.main(pyc_files)

setup(script_args=['build_ext', '--inplace'], ext_modules=cythonize(py_files))
