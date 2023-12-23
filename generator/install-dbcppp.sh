#!/bin/bash
# git clone --recurse-submodules https://github.com/xR3b0rn/dbcppp.git
cd dbcppp
# mkdir build
cd build

cmake -DCMAKE_BUILD_TYPE=Release ..
make -j
make RunTests