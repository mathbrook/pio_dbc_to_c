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



user_dbc_file =  env.subst(env.GetProjectOption("user_dbc", ""))
dbc_file = fs.match_src_files(project_dir, user_dbc_file)
dir_dbc_path = os.path.dirname(os.path.realpath(user_dbc_file))

if not len(dbc_file):
    print("[nanopb] ERROR: No file matched pattern:")
    print(f"user_dbcs: {user_dbc_file}")
    exit(1)

print(subprocess.Popen(["docker run --rm -v "+dir_dbc_path+":/app/data  /app/build/dbcppp /app/data/"+os.path.basename(dbc_file)], stdout=subprocess.PIPE))
print("hello from lib2")
