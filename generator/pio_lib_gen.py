# TODO get and build dbcppp if needed
# TODO get dbc file from url or local file
# TODO run dbcppp on supplied dbc file

import os
import hashlib
import pathlib

import subprocess

import SCons.Action
from platformio import fs

# based on https://github.com/nanopb/nanopb/blob/master/generator/platformio_generator.py

Import("env")

python_exe = env.subst("$PYTHONEXE")
project_dir = env.subst("$PROJECT_DIR")
build_dir = env.subst("$BUILD_DIR")

generated_src_dir = os.path.join(build_dir, 'dbcppp', 'generated-src')

print("hello from lib")