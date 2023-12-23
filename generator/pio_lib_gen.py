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
generated_build_dir = os.path.join(build_dir, 'dbcppp', 'generated-build')

def install_dbcppp():
    try:
        print(subprocess.Popen(["./install-dbcppp.sh"], stdout=subprocess.PIPE))
    except OSError as error:
        print("ERROR occured while trying to install dep")
try:
    subprocess.Popen(["cmake"], stdout = subprocess.PIPE)
    print("you have cmake installed")
except OSError as error:
    print("ERROR install cmake")

try:
    subprocess.Popen([build_dir+"/dbcppp-bin/dbcppp"], stdout = subprocess.PIPE)
except OSError as error:
    print("[pio_lib_gen] Installing dependencies");
    install_dbcppp()


user_dbc_files =  env.subst(env.GetProjectOption("user_dbcs", ""))

dbc_files = fs.match_src_files(project_dir, user_dbc_files)
if not len(dbc_files):
    print("[nanopb] ERROR: No files matched pattern:")
    print(f"user_dbcs: {user_dbc_files}")
    exit(1)

print("hello from lib2")
