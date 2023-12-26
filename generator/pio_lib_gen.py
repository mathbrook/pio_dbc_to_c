# TODO get and build dbcppp if needed
# TODO get dbc file from url or local file
# TODO run dbcppp on supplied dbc file

import os
import hashlib
import pathlib

import subprocess

import docker
import SCons.Action
from platformio import fs

# based on https://github.com/nanopb/nanopb/blob/master/generator/platformio_generator.py

Import("env")

python_exe = env.subst("$PYTHONEXE")
project_dir = env.subst("$PROJECT_DIR")
build_dir = env.subst("$BUILD_DIR")

generated_src_dir = os.path.join(build_dir, 'dbcppp', 'generated-src')
generated_build_dir = os.path.join(build_dir, 'dbcppp', 'generated-build')

user_dbc_file =  env.subst(env.GetProjectOption("user_dbc", ""))
drvname=  env.subst(env.GetProjectOption("drvname", ""))
dbc_file = fs.match_src_files(project_dir, user_dbc_file)
rel_dir_dbc_path = os.path.dirname(dbc_file[0])

dbc_file_name = os.path.basename(dbc_file[0])

if not len(dbc_file):
    print("[nanopb] ERROR: No file matched pattern:")
    print(f"user_dbcs: {user_dbc_file}")
    exit(1)

print("yo")
print(user_dbc_file)

abs_path_to_dbc = project_dir+'/'+rel_dir_dbc_path

print(abs_path_to_dbc)
print(generated_src_dir)
client = docker.from_env()

client.containers.run('ghcr.io/rcmast3r/ccoderdbc:main', './build/coderdbc -rw -noconfig -dbc /data/hytech.dbc -out /out -drvname '+drvname, user=os.getuid(),volumes=[abs_path_to_dbc+":/data", generated_src_dir+":/out"], working_dir='/app')
# client.containers.run('ghcr.io/rcmast3r/ccoderdbc:main', 'find /out -type d -exec chmod 755 {} \;', volumes=[abs_path_to_dbc+":/data", generated_src_dir+":/out"], working_dir='/app')
# client.containers.run('ghcr.io/rcmast3r/ccoderdbc:main', 'chmod 755 /out', volumes=[abs_path_to_dbc+":/data", generated_src_dir+":/out"], working_dir='/app')

print("hello from lib2")
